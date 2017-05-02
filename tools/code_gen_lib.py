#!/bin/env python
import json
import sys
import cpp_code_gen as cpp


def struct_member_desc(name, word_size, endianness, array_size=None, overhide_type=None):
    member = {}
    member["name"] = name
    member["word_size"] = word_size
    member["endianness"] = endianness
    member["array_size"] = array_size
    member["overhide_type"] = overhide_type
    return member

class Struct_member(object):
    def __init__(self, data_dict):
        self.name = data_dict["name"]
        self.word_size = data_dict["word_size"]
        self.endianness = data_dict["endianness"]
        self.array_size = data_dict["array_size"]
        self.overhide_type = data_dict["overhide_type"]

