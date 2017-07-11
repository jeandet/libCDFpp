project('shared lib', 'cpp')


structgen = find_program('tools/code_gen.py')

gen_src = custom_target('gen-cdf-structs',
                        input : ['src/Cdf_Structs.h.in'],
                        output : ['Cdf_Structs.h'],
                        command : [structgen, '@INPUT@',
                                   '@OUTPUT0@'])

inc = include_directories('include')

libCDFp=shared_library('libCDF++', 'src/Cdf_Private.cpp', 'src/libCDF++.cpp',
	gen_src,
	include_directories : inc,
	version : '1.0.0',
	soversion : '0')


gtest = dependency('gtest', main : true)
data_dir = '-DTEST_DATA_DIR="@0@/tests/DATA"'.format(meson.current_source_dir())
test_list = ['SimpleOpen','ObjectFeatures','CDF_Desc_Record']

foreach tst : test_list
	exe = executable('@0@Test'.format(tst),
	 	'tests/@0@/main.cpp'.format(tst),
	 	include_directories : inc,
	 	dependencies : gtest,
	 	cpp_args : data_dir,
	 	link_with : libCDFp)

	test('@0@ test'.format(tst), exe)
endforeach

