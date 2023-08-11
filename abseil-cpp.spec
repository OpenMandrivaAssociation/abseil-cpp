%define cxxstd 20
%global optflags %{optflags} -O3

%define soname %(echo %{version} |cut -b3-6).0.0
%define devname %mklibname absl -d

Name:		abseil-cpp
Version:	20230802.0
Release:	1
Summary:	C++ Common Libraries
Group:		Development/C++
License:	ASL 2.0
URL:		https://abseil.io
Source0:	https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja

%global libs base bad_any_cast_impl log_severity bad_optional_access\\\
	malloc_internal bad_variant_access periodic_sampler random_distributions\\\
	city random_internal_distribution_test_util civil_time\\\
	random_internal_platform cord random_internal_pool_urbg\\\
	debugging_internal random_internal_randen_hwaes_impl\\\
	demangle_internal random_internal_randen_hwaes examine_stack\\\
	random_internal_randen_slow exponential_biased random_internal_randen\\\
	failure_signal_handler random_internal_seed_material\\\
	flags_commandlineflag_internal random_seed_gen_exception\\\
	flags_commandlineflag random_seed_sequences flags_config\\\
	raw_hash_set flags_internal raw_logging_internal flags_marshalling\\\
	scoped_set_env flags_parse spinlock_wait flags_private_handle_accessor\\\
	stacktrace flags_program_name statusor flags_reflection status flags\\\
	strerror flags_usage_internal str_format_internal flags_usage\\\
	strings_internal graphcycles_internal strings hash symbolize\\\
	hashtablez_sampler synchronization int128 throw_delegate time\\\
	leak_check time_zone cord_internal cordz_functions cordz_handle\\\
	cordz_info cordz_sample_token low_level_hash

# Added in 20230125.1
%global libs %{libs} crc32c crc_cord_state crc_cpu_detect crc_internal die_if_null\\\
	log_entry log_flags log_globals log_initialize log_internal_check_op\\\
	log_internal_conditions log_internal_format log_internal_globals\\\
	log_internal_log_sink_set log_internal_message log_internal_nullguard\\\
	log_internal_proto log_sink

# Added in 20230802.0
%global libs %{libs} kernel_timeout_internal string_view

%(for i in %{libs}; do
	cat <<EOF
%package -n %{mklibname absl_${i}}
Summary:	The ${i} library, part of %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname absl_${i} 0} < %{EVRD}

%description -n %{mklibname absl_${i}}
The ${i} library, part of %{name}

%files -n %{mklibname absl_${i}}
%{_libdir}/libabsl_${i}.so.%{soname}
EOF
done)

#---------------------------------------------------------------------------

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
%(for i in %{libs}; do
	echo Requires: %{mklibname absl_${i}} = %{EVRD}
done)
Obsoletes:	%{_lib}absl_leak_check_disable < %{EVRD}
Obsoletes:	%{_lib}absl_wyhash < %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development headers for %{name}.

%files -n %{devname}
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1

LDFLAGS="%{optflags} -std=gnu++%{cxxstd}" \
%cmake \
	-DCMAKE_CXX_STANDARD=%{cxxstd} \
	-DABSL_CXX_STANDARD=%{cxxstd} \
	-DABSL_PROPAGATE_CXX_STD:BOOL=ON \
	-G Ninja

%build
%ninja_build -v -C build

%install
%ninja_install -C build
