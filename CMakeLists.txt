project(cmake_wrapper)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

message("*** Conan CMake Wrapper ***")
include(conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(c-ares-cares-1_14_0)
