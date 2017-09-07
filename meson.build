project('libCDF++', 'cpp')


structgen = find_program('tools/code_gen.py')

gen_src = custom_target('gen-cdf-structs',
                        input : ['src/Cdf_Structs.h.in'],
                        output : ['Cdf_Structs.h'],
                        command : [structgen, '@INPUT@','@OUTPUT0@'])

inc = include_directories('include')

libCDFpp_lib=library('libCDF++', 'src/Cdf_Private.cpp', 'src/libCDF.cpp',
	gen_src,
	include_directories : inc,
	cpp_args : ['-std=c++14'],
	version : '1.0.0',
	soversion : '0')

libCDFpp = declare_dependency(link_with : libCDFpp_lib,
                                include_directories : inc,
                                compile_args : '-std=c++14')


gtest_dep = dependency('gtest', required : false, main : false, fallback:['gtest','gtest_mainless_dep'])


data_dir = '-DTEST_DATA_DIR="@0@/tests/DATA"'.format(meson.current_source_dir())
test_list = ['SimpleOpen','ObjectFeatures','CDF_Desc_Record']

foreach tst : test_list
	exe = executable('@0@Test'.format(tst),
	 	'tests/@0@/main.cpp'.format(tst),
	 	dependencies : [gtest_dep, libCDFpp],
	 	cpp_args : data_dir)

	test('@0@ test'.format(tst), exe)
endforeach

