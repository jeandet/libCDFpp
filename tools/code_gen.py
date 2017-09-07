#!/usr/bin/env python
import json
import sys
from code_gen_lib import *
import cpp_code_gen as cpp


def main(argv):
    if len(argv) == 2:
        inputfile = argv[0]
        outputfile = argv[1]
        with open(inputfile, "r") as file:
            CDF_Structs = json.load(file)
            generator=cpp.code_gen()
            generated_code = """
//#########################################################################
/*
    This file is auto generated, do not try to edit it!
*/
//#########################################################################
            """
            generated_code+=generator.header()
            for struct in CDF_Structs:
                generated_code += generator.declare_struct(struct, CDF_Structs[struct])

            generated_code+=generator.before_mapper()
            for struct in CDF_Structs:
                generated_code += generator.declare_mapper(struct, CDF_Structs[struct])
            generated_code +=generator.footer()
            with open(outputfile, "w") as outfile:
                outfile.write(generated_code)

if __name__ == "__main__":
    main(sys.argv[1:])
