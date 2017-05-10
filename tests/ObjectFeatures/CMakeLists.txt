cmake_minimum_required (VERSION 2.6)
project (test_ObjectFeatures)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING
      "Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel." FORCE)
endif(NOT CMAKE_BUILD_TYPE)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(SOURCES
    main.cpp
    )


add_executable(test_ObjectFeatures ${SOURCES})
if(coverage)
    target_link_libraries(test_ObjectFeatures gcov)
endif()
target_link_libraries(test_ObjectFeatures gtest gtest_main)
target_link_libraries(test_ObjectFeatures gmock gmock_main)
target_link_libraries(test_ObjectFeatures libCDF++)
add_test(NAME test-ObjectFeatures COMMAND test_ObjectFeatures)
