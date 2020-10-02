#!/bin/bash
set -eoux pipefail
###
 # @Github: https://github.com/Certseeds/CS323-Compilers
 # @Organization: SUSTech
 # @Author: nanoseeds
 # @Date: 2020-09-23 01:30:40
 # @LastEditors: nanoseeds
 # @LastEditTime: 2020-10-02 20:06:37
### 
#! on work on ubuntu1804!
CMAKE_DIR="cmake-build-debug"
cmake_ensure_dir() {
  if [[ ! -d "${CMAKE_DIR}" ]]; then
    mkdir "${CMAKE_DIR}"
  fi
}
compiler() {
  cd "${CMAKE_DIR}"
  cmake ..
  make -j "$(nproc)"
  cd ..
}
run_test() {
  python3 ./calc_test.py
}
cmake_ensure_dir
compiler
run_test
