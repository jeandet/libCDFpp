#!/bin/env python
import json
import sys


def struct_member(name, word_size, endianness, array_size=None, overhide_type=None):
    member = {}
    member["name"] = name
    member["word_size"] = word_size
    member["endianness"] = endianness
    member["array_size"] = array_size
    member["overhide_type"] = overhide_type
    return member

class cdf_block_struct_member(object):
    def __init__(self, data_dict):
        self.name = data_dict["name"]
        self.word_size = data_dict["word_size"]
        self.endianness = data_dict["endianness"]
        self.array_size = data_dict["array_size"]
        self.overhide_type = data_dict["overhide_type"]


structs = {}
wonrds_types_LUT = {1:"int8_t",2:"int16_t",4:"int32_t",8:"int64_t"}
wonrds_endianness_swap_LUT = {
    2:"static_cast<int16_t>(__bswap_16(static_cast<uint16_t>(",
    4:"static_cast<int32_t>(__bswap_32(static_cast<uint32_t>(",
    8:"static_cast<int64_t>(__bswap_64(static_cast<uint64_t>("
}

def declare_struct_member(struct_member):
    type_name = struct_member.overhide_type
    name = struct_member.name
    if type_name is None:
        type_name = wonrds_types_LUT[struct_member.word_size]
    if not struct_member.array_size is None:
        name += "[{size}]".format(size=struct_member.array_size)
    return """    {type_name} {name};
    """.format(type_name=type_name, name=name)

def declare_struct(name, struct):
    if name in structs:
        raise Exception("error overhiding structure {name}".format(name=name))
    structs[name] = struct
    members = ""
    for member in struct:
        members += declare_struct_member(cdf_block_struct_member(member))
    return """
    typedef struct __attribute__((__packed__)) {typename}
    {{
    {members}
    }}{typename};
    """.format(typename=name, members=members)

def swap_endianness(member):
    if not member.array_size is None:
        return"""
            for(int idx=0;idx<{size};idx++)
                {{
                    block->{name}[idx]={swap}block->{name}[idx])));
                }}""".format(size=member.array_size,
                             name=member.name,
                             swap=wonrds_endianness_swap_LUT[member.word_size])
    else:
        return """
            block->{name}={swap}block->{name})));""".format(
                name=member.name, swap=wonrds_endianness_swap_LUT[member.word_size])

def declare_mapper(name, struct):
    typename = name
    LE_FIX = ""
    BE_FIX = ""
    for member in struct:
        member = cdf_block_struct_member(member)
        if member.endianness == "Big":
            LE_FIX += swap_endianness(member);
        if member.endianness == "Little":
            BE_FIX += swap_endianness(member);
    return """
    template<>
    inline {typename}* mapCDFBlock<{typename}>(char* data,int offset)
    {{
        {typename}* block=reinterpret_cast<{typename}*>(data+offset);
        #if __BYTE_ORDER == __LITTLE_ENDIAN
        {LE_FIX}
        #endif
        #if __BYTE_ORDER == __BIG_ENDIAN
        {BE_FIX}
        #endif
        return block;
    }}
    """.format(typename=typename, LE_FIX=LE_FIX, BE_FIX=BE_FIX)

def main(argv):
    if len(argv) == 2:
        inputfile = argv[0]
        outputfile = argv[1]
        with open(inputfile, "r") as file:
            CDF_Structs = json.load(file)
            generated_cpp = """
//#########################################################################
/*
    This file is auto generated, do not try to edit it!
*/
//#########################################################################
#ifndef CDF_STRUCTS_H
#define CDF_STRUCTS_H
#include <stdint.h>
#include <byteswap.h>
#include <endian.h>
//=========================================================================
//  Structures declarations
//=========================================================================
            """
            for struct in CDF_Structs:
                generated_cpp += declare_struct(struct, CDF_Structs[struct])

            generated_cpp += """
            template<typename CDF_Block>
            CDF_Block* mapCDFBlock(char* data,int offset=0)=delete;

            """
            for struct in CDF_Structs:
                generated_cpp += declare_mapper(struct, CDF_Structs[struct])
            generated_cpp += """
            #endif //CDF_STRUCTS_H
            """
            with open(outputfile, "w") as outfile:
                outfile.write(generated_cpp)

if __name__ == "__main__":
    main(sys.argv[1:])
