#!/bin/env python
import json
import sys
import code_gen

CDF = {
    "CDFMagic_t":
    [
        code_gen.struct_member("Magic1", 4, "Big"),
        code_gen.struct_member("Magic2", 4, "Big")
    ],
    "CDFDescriptorRecord_t":
    [
        code_gen.struct_member("size", 8, "Big"),
        code_gen.struct_member("type", 4, "Big"),
        code_gen.struct_member("GDRoffset", 8, "Big"),
        code_gen.struct_member("version", 4, "Big"),
        code_gen.struct_member("release", 4, "Big"),
        code_gen.struct_member("encoding", 4, "Big"),
        code_gen.struct_member("flags", 4, "Big"),
        code_gen.struct_member("rfuA", 4, "Big"),
        code_gen.struct_member("rfuB", 4, "Big"),
        code_gen.struct_member("increment", 4, "Big"),
        code_gen.struct_member("rfuD", 4, "Big"),
        code_gen.struct_member("rfuE", 4, "Big"),
        code_gen.struct_member("copyright", None, None, 256, "char")
    ],
    "CDFCompressedRecord_t":
    [
        code_gen.struct_member("size", 8, "Big"),
        code_gen.struct_member("type", 4, "Big"),
        code_gen.struct_member("CPRoffset", 8, "Big"),
        code_gen.struct_member("uSize", 8, "Big"),
        code_gen.struct_member("rfuA", 4, "Big")
    ],
    "CDFCompressedParametersRecord_t":
    [
        code_gen.struct_member("size", 8, "Big"),
        code_gen.struct_member("type", 4, "Big"),
        code_gen.struct_member("cType", 4, "Big"),
        code_gen.struct_member("rfuA", 8, "Big"),
        code_gen.struct_member("pCount", 4, "Big"),
        code_gen.struct_member("cParms", 4, "Big")
    ]
}

def main(argv):
    if len(argv) == 1:
        outputfile = argv[0]
        with open(outputfile, "w") as file:
            json.dump(CDF, file, indent=True)


if __name__ == "__main__":
    main(sys.argv[1:])
