# header begin
cmake_minimum_required(VERSION 3.16.6)
project(CS323_Compilers LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
# header end
# add library begin
#add_library(catch STATIC catch.hpp )
#SET_TARGET_PROPERTIES(catch PROPERTIES LINKER_LANGUAGE CXX)
add_subdirectory(./lab01)
add_subdirectory(./lab02)
add_subdirectory(./lab03)
add_subdirectory(./lab04)
add_subdirectory(./project1)