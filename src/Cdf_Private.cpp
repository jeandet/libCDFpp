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
#include "Cdf_Private.h"
#include <iostream>
#include <fstream>
#include <limits>
#include <libCDF.h>
#include <Cdf_Structs.h>

bool p_checkMagic(const CDFMagic_t& magic);
bool p_isCompressed(const CDFMagic_t& magic);

Cdf_Private::Cdf_Private() {}

Cdf_Private::Cdf_Private(const std::string &fname, std::fstream::openmode mode)
    :fname(fname)
{
    this->open(fname,mode);
}

//might be refactored later
inline std::streamsize fileSize(std::fstream& file)
{
    file.ignore(std::numeric_limits<std::streamsize>::max());
    std::streamsize length = file.gcount();
    file.clear();
    file.seekg( 0, std::ios_base::beg );
    return length;
}


bool Cdf_Private::open(const std::string &fname, std::fstream::openmode mode)
{
    this->opened=false;
    this->compressed=false;
    std::fstream cdfFile(fname, std::fstream::binary | mode);
    if(cdfFile.is_open())
    {
        this->fname = fname;
        std::streamsize length = fileSize(cdfFile);
        if(length>=static_cast<long>(8))
        {
            this->opened=true;
            std::shared_ptr<char> data(new char[static_cast<unsigned long>(length)], std::default_delete<char[]>());
            cdfFile.read(&(data.get()[0]),length);
            auto magic=mapCDFBlock<CDFMagic_t>(data);
            this->opened=p_checkMagic(magic);
            if(this->opened)
            {
                this->compressed=p_isCompressed(magic);

            }
        }
    }
    return this->opened;
}


bool p_isCompressed(const CDFMagic_t& magic)
{
    return  magic->Magic2 == 0xCCCC0001;
}

bool p_checkMagic(const CDFMagic_t& magic)
{
    return ( (magic->Magic1&0xCDF00000)==0xCDF00000
             &&
             (magic->Magic2 == 0x0000FFFF //Uncompressed
              ||
              magic->Magic2 == 0xCCCC0001)); //Compressed

}
