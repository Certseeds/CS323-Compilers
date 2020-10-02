#!/usr/bin/env python3
# coding=utf-8
'''
Github: https://github.com/Certseeds/CS323-Compilers
Organization: SUSTech
Author: nanoseeds
Date: 2020-09-30 01:49:33
LastEditors: nanoseeds
LastEditTime: 2020-10-02 23:00:23
'''
import pathlib
import re
import subprocess


DATA = pathlib.Path('data')


def jsonparser_output(json_file):
    out = subprocess.check_output(['./cmake-build-debug/CS323_Compilers_lab04_json_jp.out', json_file])
    return out.decode().strip()


def check_jsonchecker_fail_withlexical():
    data = DATA
    for failjson in data.glob('fail*.json'):
        out = jsonparser_output(failjson)
        if ('lexical error' not in out) or ('_EXCLUDE' in failjson.name):
            continue
        print(f'For file {failjson.name}:')
        print(out)
        print('-'*80)


def check_jsonchecker_fail_syntaxonly():
    data = DATA
    recovered, total = 0, 0
    for failjson in data.glob('fail*.json'):
        out = jsonparser_output(failjson)
        if ('lexical error' in out) or ('_EXCLUDE' in failjson.name):
            continue
        print(f'For file {failjson.name}:')
        print('-'*24)
        print(open(failjson).read())
        print('-'*80)
        print(out)
        print('#'*80)
        m = re.match(r'^syntax(.*?)recovered$', out)
        recovered += bool(m)
        total += 1
    print(f'Recovered/Total: {recovered}/{total}')



# check_jsonchecker_fail_withlexical()
check_jsonchecker_fail_syntaxonly()
