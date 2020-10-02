# header begin
cmake_minimum_required(VERSION 3.16.6)
project(CS323_lab02 LANGUAGES C CXX)

# header end
# add library begin
#add_library(catch STATIC catch.hpp )
#SET_TARGET_PROPERTIES(catch PROPERTIES LINKER_LANGUAGE CXX)
add_subdirectory(./ipaddr)
add_subdirectory(./wc)