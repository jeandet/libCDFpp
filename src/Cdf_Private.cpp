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
#include <libCDF++.h>

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
    std::fstream cdfFile(fname, std::fstream::binary | mode);
    if(cdfFile.is_open())
    {
        this->fname = fname;
        std::streamsize length = fileSize(cdfFile);
        if(length>=static_cast<long>(MIN_CDF_SIZE))
        {
            this->opened=true;
            char* data=new char[static_cast<unsigned long>(length)];
            cdfFile.read(data,length);
            toMachineEndianness(data);
            CDF_t* cdfFile=(CDF_t*)data;
            this->opened=p_checkMagic(cdfFile);
            if(this->opened)
            {

            }
            delete[] data;
        }
    }
    return this->opened;
}

bool Cdf_Private::p_checkMagic(const CDF_t *file)
{
    return ( (file->magicNumbers.Magic1&0xCDF00000)==0xCDF00000
             &&
             (file->magicNumbers.Magic2 == 0x0000FFFF //Uncompressed
              ||
              file->magicNumbers.Magic2 == 0xCCCC0001)); //Compressed

}
