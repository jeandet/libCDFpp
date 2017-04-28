cmake_minimum_required (VERSION 2.6)
project (test_SimpleOpen)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING
      "Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif(NOT CMAKE_BUILD_TYPE)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(SOURCES
    main.cpp
    )


add_executable(test_SimpleOpen ${SOURCES})
target_link_libraries(test_SimpleOpen gtest gtest_main)
target_link_libraries(test_SimpleOpen gmock gmock_main)
target_link_libraries(test_SimpleOpen libCDF++)
add_test(NAME test-SimpleOpen COMMAND test_SimpleOpen)
