/*------------------------------------------------------------------------------
--  This file is a part of the libCDF++ library
--  Copyright (C) 2017, Plasma Physics Laboratory - CNRS
--
--  This program is free software; you can redistribute it and/or modify
--  it under the terms of the GNU General Public License as published by
--  the Free Software Foundation; either version 2 of the License, or
--  (at your option) any later version.
--
--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU General Public License for more details.
--
--  You should have received a copy of the GNU General Public License
--  along with this program; if not, write to the Free Software
--  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
-------------------------------------------------------------------------------*/
/*--                 Author : Alexis Jeandet
--                     Mail : alexis.jeandet@member.fsf.org
----------------------------------------------------------------------------*/
#ifndef CDF_STRUCTS_H
#define CDF_STRUCTS_H
#include <stdint.h>
#include <byteswap.h>
#include <vector>
#include <tuple>

typedef struct __attribute__((__packed__)) CDFMagic_t
{
    uint32_t Magic1;
    uint32_t Magic2;
}CDFMagic_t;

typedef struct __attribute__((__packed__)) CDFDescriptorRecord_t
{
    int64_t size;
    int32_t type;
    int64_t GDRoffset;
    int32_t version;
    int32_t release;
    int32_t encoding;
    int32_t flags;
    int32_t rfuA;
    int32_t rfuB;
    int32_t increment;
    int32_t rfuD;
    int32_t rfuE;
    char copyright[256];//Only compatible with 2.5+ CDF version
}CDFDescriptorRecord_t;

typedef struct __attribute__((__packed__)) CDF_t
{
    CDFMagic_t magicNumbers;
    CDFDescriptorRecord_t CDFDescriptorRecord;
}CDF_t;

#define MIN_CDF_SIZE (sizeof(CDFMagic_t) + sizeof(CDFDescriptorRecord_t))

template<int T>
inline void fixEndianness(char* data)=delete;

template <>
inline void fixEndianness<2>(char* data)
{
    uint16_t* word=reinterpret_cast<uint16_t*>(data);
    *word=__bswap_16(*word);
}
template <>
inline void fixEndianness<4>(char* data)
{
    uint32_t* word=reinterpret_cast<uint32_t*>(data);
    *word=__bswap_32(*word);
}
template<>
inline void fixEndianness<8>(char* data)
{
    uint64_t* word=reinterpret_cast<uint64_t*>(data);
    *word=__bswap_64(*word);
}

inline void toMachineEndianness(char* file)
{
#if __BYTE_ORDER == __LITTLE_ENDIAN
    std::vector<std::pair<bool,int>> wordsMap={
        {true,4},
        {true,4},
        {true,8},
        {true,4},
        {true,8},
        {true,4},
        {true,4},
        {true,4},
        {true,4},
        {true,4},
        {true,4},
        {true,4},
        {true,4},
        {true,4},
        {false,256}
    };
    if(file!=nullptr)
    {
        for(const auto& word:wordsMap)
        {
            if(word.first)
            {
                switch (word.second)
                {
                case 2:
                    fixEndianness<2>(file);
                    break;
                case 4:
                    fixEndianness<4>(file);
                    break;
                case 8:
                    fixEndianness<8>(file);
                    break;
                default:
                    break;
                }
            }
            file+=word.second;
        }
    }
#endif
}
#endif
