#!/bin/env python
import json
import sys
import code_gen_lib as code_gen

CDF = {
    "CDFMagic_t":
    [
        code_gen.struct_member_desc("Magic1", 4, "Big"),
        code_gen.struct_member_desc("Magic2", 4, "Big")
    ],
    "CDFDescriptorRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("GDRoffset", 8, "Big"),
        code_gen.struct_member_desc("version", 4, "Big"),
        code_gen.struct_member_desc("release", 4, "Big"),
        code_gen.struct_member_desc("encoding", 4, "Big"),
        code_gen.struct_member_desc("flags", 4, "Big"),
        code_gen.struct_member_desc("rfuA", 4, "Big"),
        code_gen.struct_member_desc("rfuB", 4, "Big"),
        code_gen.struct_member_desc("increment", 4, "Big"),
        code_gen.struct_member_desc("rfuD", 4, "Big"),
        code_gen.struct_member_desc("rfuE", 4, "Big"),
        code_gen.struct_member_desc("copyright", None, None, 256, "char")
    ],
    "CDFCompressedRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("CPRoffset", 8, "Big"),
        code_gen.struct_member_desc("uSize", 8, "Big"),
        code_gen.struct_member_desc("rfuA", 4, "Big")
    ],
    "CDFCompressedParametersRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("cType", 4, "Big"),
        code_gen.struct_member_desc("rfuA", 8, "Big"),
        code_gen.struct_member_desc("pCount", 4, "Big"),
        code_gen.struct_member_desc("cParms", 4, "Big")
    ],
    "CDFGlobalDescriptorRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("rVDRhead", 8, "Big"),
        code_gen.struct_member_desc("zVDRhead", 8, "Big"),
        code_gen.struct_member_desc("ADRhead", 8, "Big"),
        code_gen.struct_member_desc("eof", 8, "Big"),
        code_gen.struct_member_desc("NrVars", 4, "Big"),
        code_gen.struct_member_desc("NumAttr", 4, "Big"),
        code_gen.struct_member_desc("rMaxRec", 4, "Big"),
        code_gen.struct_member_desc("rNumDims", 4, "Big"),
        code_gen.struct_member_desc("NzVars", 4, "Big"),
        code_gen.struct_member_desc("UIRhead", 8, "Big"),
        code_gen.struct_member_desc("rfuC", 4, "Big"),
        code_gen.struct_member_desc("LeapSecondLastUpdated", 4, "Big"),
        code_gen.struct_member_desc("rfuE", 4, "Big")
    ],
    "CDFAttributeDecriptorRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("ADRnext", 8, "Big"),
        code_gen.struct_member_desc("AgrEDRhead", 8, "Big"),
        code_gen.struct_member_desc("Scope", 4, "Big"),
        code_gen.struct_member_desc("Num", 4, "Big"),
        code_gen.struct_member_desc("NgrEntries", 4, "Big"),
        code_gen.struct_member_desc("MAXgrEntries", 4, "Big"),
        code_gen.struct_member_desc("rfua", 4, "Big"),
        code_gen.struct_member_desc("AzEDRhead", 8, "Big"),
        code_gen.struct_member_desc("NzEntries", 4, "Big"),
        code_gen.struct_member_desc("MAXzEntry", 4, "Big"),
        code_gen.struct_member_desc("rfuE", 4, "Big"),
        code_gen.struct_member_desc("Name", None, None, 256, "char")
    ],
    "CDFAttributeEntryDecriptorRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("AEDRnext", 8, "Big"),
        code_gen.struct_member_desc("AttrNum", 4, "Big"),
        code_gen.struct_member_desc("DataType", 4, "Big"),
        code_gen.struct_member_desc("Num", 4, "Big"),
        code_gen.struct_member_desc("NumElements", 4, "Big"),
        code_gen.struct_member_desc("rfuA", 4, "Big"),
        code_gen.struct_member_desc("rfuB", 4, "Big"),
        code_gen.struct_member_desc("rfuC", 4, "Big"),
        code_gen.struct_member_desc("rfuD", 4, "Big"),
        code_gen.struct_member_desc("rfuE", 4, "Big")
    ],
    "CDFVariableDecriptorRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("VDRnext", 8, "Big"),
        code_gen.struct_member_desc("DataType", 4, "Big"),
        code_gen.struct_member_desc("MaxRec", 4, "Big"),
        code_gen.struct_member_desc("VXRhead", 8, "Big"),
        code_gen.struct_member_desc("VXRtail", 8, "Big"),
        code_gen.struct_member_desc("Flags", 4, "Big"),
        code_gen.struct_member_desc("SRecords", 4, "Big"),
        code_gen.struct_member_desc("rfuB", 4, "Big"),
        code_gen.struct_member_desc("rfuC", 4, "Big"),
        code_gen.struct_member_desc("rfuF", 4, "Big"),
        code_gen.struct_member_desc("NumElements", 4, "Big"),
        code_gen.struct_member_desc("Num", 4, "Big"),
        code_gen.struct_member_desc("CPRorSPRoffset", 8, "Big"),
        code_gen.struct_member_desc("BlockingFactor", 4, "Big"),
        code_gen.struct_member_desc("Name", None, None, 256, "char")
    ],
    "CDFVariableIndexRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("VXRnext", 8, "Big"),
        code_gen.struct_member_desc("Nentries", 4, "Big"),
        code_gen.struct_member_desc("NusedEntries", 4, "Big")
    ],
    "CDFVariableValuesRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big")
    ],
    "CDFSparsnessParametersRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("sArraysType", 4, "Big"),
        code_gen.struct_member_desc("rfuA", 4, "Big"),
        code_gen.struct_member_desc("pCount", 4, "Big")
    ],
    "CDFCompressedVariableValuesRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("rfuA", 4, "Big"),
        code_gen.struct_member_desc("cSize", 8, "Big")
    ],
    "CDFUnusedInternalRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big"),
        code_gen.struct_member_desc("NextUIR", 8, "Big"),
        code_gen.struct_member_desc("PrevUIR", 8, "Big")
    ],
    "CDFUnasociableUnusedInternalRecord_t":
    [
        code_gen.struct_member_desc("size", 8, "Big"),
        code_gen.struct_member_desc("type", 4, "Big")
    ]
}

def main(argv):
    if len(argv) == 1:
        outputfile = argv[0]
        with open(outputfile, "w") as file:
            json.dump(CDF, file, indent=True)


if __name__ == "__main__":
    main(sys.argv[1:])
