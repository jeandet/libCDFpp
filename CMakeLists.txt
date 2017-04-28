cmake_minimum_required (VERSION 2.6)
project (libCDF++)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING
      "Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif(NOT CMAKE_BUILD_TYPE)

set (CMAKE_CXX_STANDARD 14)

set(SOURCES
    src/libCDF++.cpp
    include/libCDF++.h
    src/Cdf_Private.cpp
    src/Cdf_Private.h
    src/Cdf_Structs.h
    )

add_library(libCDF++ ${SOURCES})

include_directories("include")

option(test "Build all tests." ON) # Makes boolean 'test' available.

if (test)

  # This adds another subdirectory, which has 'project(gtest)'.
  add_subdirectory(googletest)
  enable_testing()

  # Include the gtest library. gtest_SOURCE_DIR is available due to
  # 'project(gtest)' above.
  include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})
  include_directories(${gmock_SOURCE_DIR}/include ${gmock_SOURCE_DIR})

  ##############
  # Unit Tests
  ##############
  add_definitions(-DTEST_DATA_DIR="${CMAKE_CURRENT_LIST_DIR}/tests/DATA")
  add_subdirectory(tests/CDF_Desc_Record)
  add_subdirectory(tests/SimpleOpen)

endif()
