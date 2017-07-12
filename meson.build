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
	default_options : ['cpp_std=c++14'],
	version : '1.0.0',
	soversion : '0')


gtest_dep = dependency('gtest', required : false, main : true)
gtest_src = []
gtest_inc = []
if not gtest_dep.found()
  gtest_proj = subproject('gtest')
  gtest_dep = [dependency('threads')]
  gtest_src = [gtest_proj.get_variable('libsources')]
  gtest_inc = gtest_proj.get_variable('incdir')
endif

data_dir = '-DTEST_DATA_DIR="@0@/tests/DATA"'.format(meson.current_source_dir())
test_list = ['SimpleOpen','ObjectFeatures','CDF_Desc_Record']

foreach tst : test_list
	exe = executable('@0@Test'.format(tst),
	 	'tests/@0@/main.cpp'.format(tst),gtest_src,
	 	include_directories : [gtest_inc, inc],
	 	dependencies : gtest_dep,
	 	cpp_args : data_dir,
	 	link_with : libCDFp)

	test('@0@ test'.format(tst), exe)
endforeach

