%define cxxstd 20
%global optflags %{optflags} -O3

%define major 0
%define devname %mklibname absl -d

Name:		abseil-cpp
Version:	20220623.1
Release:	1
Summary:	C++ Common Libraries
Group:		Development/C++
License:	ASL 2.0
URL:		https://abseil.io
Source0:	https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		abseil-cpp-20210324.1-revert-soversion-to-0.patch
BuildRequires:	cmake
BuildRequires:	ninja

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

%define local_lib_pkg() %{expand:\
%package -n %{mklibname absl_%1} \
Summary:	%{summary} \
Group:		System/Libraries \
%rename %{mklibname absl_%1 0} \
%description -n %{mklibname absl_%1} \
%{summary} .\
Package with library libsbsl_%{1}.so.%{major}. \
%files -n %{mklibname absl_%1} \
%{_libdir}/libabsl_%{1}.so.%{major} \
}

%local_lib_pkg base
%local_lib_pkg bad_any_cast_impl
%local_lib_pkg log_severity
%local_lib_pkg bad_optional_access
%local_lib_pkg malloc_internal
%local_lib_pkg bad_variant_access
%local_lib_pkg periodic_sampler
%local_lib_pkg random_distributions
%local_lib_pkg city
%local_lib_pkg random_internal_distribution_test_util
%local_lib_pkg civil_time
%local_lib_pkg random_internal_platform
%local_lib_pkg cord
%local_lib_pkg random_internal_pool_urbg
%local_lib_pkg debugging_internal
%local_lib_pkg random_internal_randen_hwaes_impl
%local_lib_pkg demangle_internal
%local_lib_pkg random_internal_randen_hwaes
%local_lib_pkg examine_stack
%local_lib_pkg random_internal_randen_slow
%local_lib_pkg exponential_biased
%local_lib_pkg random_internal_randen
%local_lib_pkg failure_signal_handler
%local_lib_pkg random_internal_seed_material
%local_lib_pkg flags_commandlineflag_internal
%local_lib_pkg random_seed_gen_exception
%local_lib_pkg flags_commandlineflag
%local_lib_pkg random_seed_sequences
%local_lib_pkg flags_config
%local_lib_pkg raw_hash_set
%local_lib_pkg flags_internal
%local_lib_pkg raw_logging_internal
%local_lib_pkg flags_marshalling
%local_lib_pkg scoped_set_env
%local_lib_pkg flags_parse
%local_lib_pkg spinlock_wait
%local_lib_pkg flags_private_handle_accessor
%local_lib_pkg stacktrace
%local_lib_pkg flags_program_name
%local_lib_pkg statusor
%local_lib_pkg flags_reflection
%local_lib_pkg status
%local_lib_pkg flags
%local_lib_pkg strerror
%local_lib_pkg flags_usage_internal
%local_lib_pkg str_format_internal
%local_lib_pkg flags_usage
%local_lib_pkg strings_internal
%local_lib_pkg graphcycles_internal
%local_lib_pkg strings
%local_lib_pkg hash
%local_lib_pkg symbolize
%local_lib_pkg hashtablez_sampler
%local_lib_pkg synchronization
%local_lib_pkg int128
%local_lib_pkg throw_delegate
%local_lib_pkg time
%local_lib_pkg leak_check
%local_lib_pkg time_zone
%local_lib_pkg cord_internal
%local_lib_pkg cordz_functions
%local_lib_pkg cordz_handle
%local_lib_pkg cordz_info
%local_lib_pkg cordz_sample_token
%local_lib_pkg low_level_hash

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{_lib}absl_base = %{EVRD}
Requires:	%{_lib}absl_bad_any_cast_impl = %{EVRD}
Requires:	%{_lib}absl_log_severity = %{EVRD}
Requires:	%{_lib}absl_bad_optional_access = %{EVRD}
Requires:	%{_lib}absl_malloc_internal = %{EVRD}
Requires:	%{_lib}absl_bad_variant_access = %{EVRD}
Requires:	%{_lib}absl_periodic_sampler = %{EVRD}
Requires:	%{_lib}absl_random_distributions = %{EVRD}
Requires:	%{_lib}absl_city = %{EVRD}
Requires:	%{_lib}absl_random_internal_distribution_test_util = %{EVRD}
Requires:	%{_lib}absl_civil_time = %{EVRD}
Requires:	%{_lib}absl_random_internal_platform = %{EVRD}
Requires:	%{_lib}absl_cord = %{EVRD}
Requires:	%{_lib}absl_random_internal_pool_urbg = %{EVRD}
Requires:	%{_lib}absl_debugging_internal = %{EVRD}
Requires:	%{_lib}absl_random_internal_randen_hwaes_impl = %{EVRD}
Requires:	%{_lib}absl_demangle_internal = %{EVRD}
Requires:	%{_lib}absl_random_internal_randen_hwaes = %{EVRD}
Requires:	%{_lib}absl_examine_stack = %{EVRD}
Requires:	%{_lib}absl_random_internal_randen_slow = %{EVRD}
Requires:	%{_lib}absl_exponential_biased = %{EVRD}
Requires:	%{_lib}absl_random_internal_randen = %{EVRD}
Requires:	%{_lib}absl_failure_signal_handler = %{EVRD}
Requires:	%{_lib}absl_random_internal_seed_material = %{EVRD}
Requires:	%{_lib}absl_flags_commandlineflag_internal = %{EVRD}
Requires:	%{_lib}absl_random_seed_gen_exception = %{EVRD}
Requires:	%{_lib}absl_flags_commandlineflag = %{EVRD}
Requires:	%{_lib}absl_random_seed_sequences = %{EVRD}
Requires:	%{_lib}absl_flags_config = %{EVRD}
Requires:	%{_lib}absl_raw_hash_set = %{EVRD}
Requires:	%{_lib}absl_flags_internal = %{EVRD}
Requires:	%{_lib}absl_raw_logging_internal = %{EVRD}
Requires:	%{_lib}absl_flags_marshalling = %{EVRD}
Requires:	%{_lib}absl_scoped_set_env = %{EVRD}
Requires:	%{_lib}absl_flags_parse = %{EVRD}
Requires:	%{_lib}absl_spinlock_wait = %{EVRD}
Requires:	%{_lib}absl_flags_private_handle_accessor = %{EVRD}
Requires:	%{_lib}absl_stacktrace = %{EVRD}
Requires:	%{_lib}absl_flags_program_name = %{EVRD}
Requires:	%{_lib}absl_statusor = %{EVRD}
Requires:	%{_lib}absl_flags_reflection = %{EVRD}
Requires:	%{_lib}absl_status = %{EVRD}
Requires:	%{_lib}absl_flags = %{EVRD}
Requires:	%{_lib}absl_strerror = %{EVRD}
Requires:	%{_lib}absl_flags_usage_internal = %{EVRD}
Requires:	%{_lib}absl_str_format_internal = %{EVRD}
Requires:	%{_lib}absl_flags_usage = %{EVRD}
Requires:	%{_lib}absl_strings_internal = %{EVRD}
Requires:	%{_lib}absl_graphcycles_internal = %{EVRD}
Requires:	%{_lib}absl_strings = %{EVRD}
Requires:	%{_lib}absl_hash = %{EVRD}
Requires:	%{_lib}absl_symbolize = %{EVRD}
Requires:	%{_lib}absl_hashtablez_sampler = %{EVRD}
Requires:	%{_lib}absl_synchronization = %{EVRD}
Requires:	%{_lib}absl_int128 = %{EVRD}
Requires:	%{_lib}absl_throw_delegate = %{EVRD}
Obsoletes:	%{_lib}absl_leak_check_disable < %{EVRD}
Requires:	%{_lib}absl_time = %{EVRD}
Requires:	%{_lib}absl_leak_check = %{EVRD}
Requires:	%{_lib}absl_time_zone = %{EVRD}
Obsoletes:	%{_lib}absl_wyhash < %{EVRD}
Requires:	%{_lib}absl_cord_internal = %{EVRD}
Requires:	%{_lib}absl_cordz_functions = %{EVRD}
Requires:	%{_lib}absl_cordz_handle = %{EVRD}
Requires:	%{_lib}absl_cordz_info = %{EVRD}
Requires:	%{_lib}absl_cordz_sample_token = %{EVRD}
Requires:	%{_lib}absl_low_level_hash = %{EVRD}
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
