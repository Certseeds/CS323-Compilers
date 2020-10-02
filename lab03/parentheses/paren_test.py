#!/usr/bin/env python3
# coding=utf-8
'''
Github: https://github.com/Certseeds/CS323-Compilers
Organization: SUSTech
Author: nanoseeds
Date: 2020-09-23 02:57:06
LastEditors: nanoseeds
LastEditTime: 2020-10-02 20:07:18
'''

import ctypes
import os
import pickle


"""
Test cases originated from:

LeetCode 20. Validate Parentheses
https://leetcode.com/problems/valid-parentheses
"""



cwd = os.getcwd()
CMAKE_DIR = "cmake-build-debug"
SO_NAME = "libCS323_Compilers_lab03_parentheses_paren.so"
lib_path = os.path.join(cwd, '{}/{}'.format(CMAKE_DIR, SO_NAME))
lib = ctypes.cdll.LoadLibrary(lib_path)

def valid_parentheses(paren):
    func = lib.validParentheses
    func.restype = ctypes.c_int32
    paren_b = paren.encode('ascii')
    paren_buf = ctypes.c_char_p(paren_b)
    return func(paren_buf)


with open('data.pickle', 'rb') as f:
    truematch, falsematch = pickle.load(f)

for input_ in truematch:
    if valid_parentheses(input_) != 1:
        print('Wrong!')
        print('Input: %s should be true' % input_)
        exit(-1)
for input_ in falsematch:
    if valid_parentheses(input_) != 0:
        print('Wrong!')
        print('Input: %s should be false' % input_)
        exit(-1)

print('All tests passed!')
