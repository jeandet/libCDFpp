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
#include "Cdf_Structs.h"

const std::vector<std::pair<bool,int>> CDFMagicWordsMap={
    {true,4},
    {true,4}
};

const std::vector<std::pair<bool,int>> CDFDescriptorRecordWordsMap={
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

const std::vector<std::pair<bool,int>> CDFCompressedRecordWordsMap={
    {true,8},
    {true,4},
    {true,8},
    {true,8},
    {true,4}
};
