cmake_minimum_required (VERSION 2.6)
project (test_CDR)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING
      "Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif(NOT CMAKE_BUILD_TYPE)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(SOURCES
    main.cpp
    )
    




add_executable(test_CDR ${SOURCES})
if(coverage)
    target_link_libraries(test_CDR gcov)
endif()
target_link_libraries(test_CDR gtest gtest_main)
target_link_libraries(test_CDR gmock gmock_main)
target_link_libraries(test_CDR libCDF++)
add_test(NAME test-CDR COMMAND test_CDR)
