#!/bin/env python
import sys
import code_gen_lib



MAPPER_DECL = """
class {typename}: public safeStructMapper<_{typename}>
{{
  public:
    {typename}(std::shared_ptr<char> data, _{typename}* structToMap)
      :safeStructMapper<_{typename}>(data,structToMap)
    {{}}
  {var_fields}
}};
template<>
inline decltype (auto) mapCDFBlock<{typename}>(std::shared_ptr<char> data,int offset)
{{
    {typename} safeStruct(data,reinterpret_cast<_{typename}*>(data.get()+offset));
    #if __BYTE_ORDER == __LITTLE_ENDIAN
    {LE_FIX}
    #endif
    #if __BYTE_ORDER == __BIG_ENDIAN
    {BE_FIX}
    #endif
    return safeStruct;
}}
        """

STRUCT_DECL = """
typedef struct __attribute__((__packed__)) {typename}
{{
{members}
}}{typename};
"""

HEADER = """
#ifndef CDF_STRUCTS_H
#define CDF_STRUCTS_H
#include <stdint.h>
#if defined(__APPLE__)
 #include <libkern/OSByteOrder.h>
 #define byte_swap_16 OSSwapInt16
 #define byte_swap_32 OSSwapInt32
 #define byte_swap_64 OSSwapInt64
 #include <machine/endian.h>
#elif defined(__MINGW32__)
   #define __bswap_16 __builtin_bswap16
   #define __bswap_32 __builtin_bswap32
   #define __bswap_64 __builtin_bswap64
#else
 #define byte_swap_16 __bswap_16
 #define byte_swap_32 __bswap_32
 #define byte_swap_64 __bswap_64
 #include <byteswap.h>
 #include <endian.h>
#endif
#include <memory>

template <typename T>
class safeStructMapper
{
    T* _mappedStruct;
    std::shared_ptr<char> data;
public:
    safeStructMapper(std::shared_ptr<char> data, T* structToMap)
        :_mappedStruct(structToMap),data(data)
    {}
    T*
    operator->() const noexcept
    {
        return _mappedStruct;
    }
};
//=========================================================================
//  Structures declarations
//=========================================================================
                """

class code_gen(object):
    def __init__(self):
        self.structs = {}
        self.words_types_LUT = {1:"uint8_t",2:"uint16_t",4:"uint32_t",8:"uint64_t"}
        self.words_endianness_swap_LUT = {
            2:"static_cast<int16_t>(byte_swap_16(static_cast<uint16_t>(",
            4:"static_cast<int32_t>(byte_swap_32(static_cast<uint32_t>(",
            8:"static_cast<int64_t>(byte_swap_64(static_cast<uint64_t>("
        }

    def header(self):
        return HEADER

    def declare_struct_member(self,struct_member):
        type_name = struct_member.overhide_type
        name = struct_member.name
        if type_name is None:
            type_name = self.words_types_LUT[struct_member.word_size]
        if not struct_member.array_size is None:
            name += "[{size}]".format(size=struct_member.array_size)
        return """    {type_name} {name};
        """.format(type_name=type_name, name=name)

    def declare_struct(self,name,struct):
        if name in self.structs:
            raise Exception("error overhiding structure {name}".format(name=name))
        self.structs[name] = struct
        members = ""
        for member in struct:
            members += self.declare_struct_member(code_gen_lib.Struct_member(member))
        return STRUCT_DECL.format(typename="_"+name, members=members)

    def swap_endianness(self,member):
        if not member.array_size is None:
            return """
                for(int idx=0;idx<{size};idx++)
                    {{
                        safeStruct->{name}[idx]={swap}safeStruct->{name}[idx])));
                    }}""".format(size=member.array_size,
                                 name=member.name,
                                 swap=self.words_endianness_swap_LUT[member.word_size])
        else:
            return """
                safeStruct->{name}={swap}safeStruct->{name})));""".format(
                    name=member.name, swap=self.words_endianness_swap_LUT[member.word_size])

    def before_mapper(self):
        return """
template<typename CDF_Block>
decltype (auto) mapCDFBlock(std::shared_ptr<char> data,int offset=0){};
            """

    def declare_mapper(self,name, struct):
        typename = name
        LE_FIX = ""
        BE_FIX = ""
        var_fields = ""
        for member in struct:
            member = code_gen_lib.Struct_member(member)
            if member.endianness == "Big":
                LE_FIX += self.swap_endianness(member);
            if member.endianness == "Little":
                BE_FIX += self.swap_endianness(member);
        return MAPPER_DECL.format(typename=typename, LE_FIX=LE_FIX, BE_FIX=BE_FIX, var_fields=var_fields)

    def footer(slef):
         return """
#endif //CDF_STRUCTS_H
        """
