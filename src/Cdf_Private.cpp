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
#include <libCDF++.h>

Cdf_Private::Cdf_Private() {}

Cdf_Private::Cdf_Private(const std::string &fname, std::fstream::openmode mode)
    :fname(fname)
{
    this->open(fname,mode);
}

bool Cdf_Private::open(const std::string &fname, std::fstream::openmode mode)
{
    this->opened=false;
    std::fstream cdfFile;
    cdfFile.open(fname, std::fstream::binary | mode);
    if(cdfFile.is_open())
    {
        this->opened=true;
        this->fname=fname;
    }
    return this->opened;
}
