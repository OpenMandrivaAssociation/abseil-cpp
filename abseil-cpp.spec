%define major 0
%define devname %mklibname absl -d

Name:		abseil-cpp
Version:	20200923.2
Release:	3
Summary:	C++ Common Libraries
Group:		Development/C++
License:	ASL 2.0
URL:		https://abseil.io
Source0:	https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	patchelf

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
%package -n %{mklibname absl_%1 0} \
Summary: %{summary} \
Group: System/Libraries \
%description -n %{mklibname absl_%1 0} \
%{summary} \
Package with library libsbsl_%{1}.so.%{major}. \
%files -n %{mklibname absl_%1 0} \
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
%local_lib_pkg leak_check_disable
%local_lib_pkg time
%local_lib_pkg leak_check
%local_lib_pkg time_zone

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires: %{_lib}absl_base%{major} = %{EVRD}
Requires: %{_lib}absl_bad_any_cast_impl%{major} = %{EVRD}
Requires: %{_lib}absl_log_severity%{major} = %{EVRD}
Requires: %{_lib}absl_bad_optional_access%{major} = %{EVRD}
Requires: %{_lib}absl_malloc_internal%{major} = %{EVRD}
Requires: %{_lib}absl_bad_variant_access%{major} = %{EVRD}
Requires: %{_lib}absl_periodic_sampler%{major} = %{EVRD}
Requires: %{_lib}absl_random_distributions%{major} = %{EVRD}
Requires: %{_lib}absl_city%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_distribution_test_util%{major} = %{EVRD}
Requires: %{_lib}absl_civil_time%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_platform%{major} = %{EVRD}
Requires: %{_lib}absl_cord%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_pool_urbg%{major} = %{EVRD}
Requires: %{_lib}absl_debugging_internal%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_randen_hwaes_impl%{major} = %{EVRD}
Requires: %{_lib}absl_demangle_internal%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_randen_hwaes%{major} = %{EVRD}
Requires: %{_lib}absl_examine_stack%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_randen_slow%{major} = %{EVRD}
Requires: %{_lib}absl_exponential_biased%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_randen%{major} = %{EVRD}
Requires: %{_lib}absl_failure_signal_handler%{major} = %{EVRD}
Requires: %{_lib}absl_random_internal_seed_material%{major} = %{EVRD}
Requires: %{_lib}absl_flags_commandlineflag_internal%{major} = %{EVRD}
Requires: %{_lib}absl_random_seed_gen_exception%{major} = %{EVRD}
Requires: %{_lib}absl_flags_commandlineflag%{major} = %{EVRD}
Requires: %{_lib}absl_random_seed_sequences%{major} = %{EVRD}
Requires: %{_lib}absl_flags_config%{major} = %{EVRD}
Requires: %{_lib}absl_raw_hash_set%{major} = %{EVRD}
Requires: %{_lib}absl_flags_internal%{major} = %{EVRD}
Requires: %{_lib}absl_raw_logging_internal%{major} = %{EVRD}
Requires: %{_lib}absl_flags_marshalling%{major} = %{EVRD}
Requires: %{_lib}absl_scoped_set_env%{major} = %{EVRD}
Requires: %{_lib}absl_flags_parse%{major} = %{EVRD}
Requires: %{_lib}absl_spinlock_wait%{major} = %{EVRD}
Requires: %{_lib}absl_flags_private_handle_accessor%{major} = %{EVRD}
Requires: %{_lib}absl_stacktrace%{major} = %{EVRD}
Requires: %{_lib}absl_flags_program_name%{major} = %{EVRD}
Requires: %{_lib}absl_statusor%{major} = %{EVRD}
Requires: %{_lib}absl_flags_reflection%{major} = %{EVRD}
Requires: %{_lib}absl_status%{major} = %{EVRD}
Requires: %{_lib}absl_flags%{major} = %{EVRD}
Requires: %{_lib}absl_strerror%{major} = %{EVRD}
Requires: %{_lib}absl_flags_usage_internal%{major} = %{EVRD}
Requires: %{_lib}absl_str_format_internal%{major} = %{EVRD}
Requires: %{_lib}absl_flags_usage%{major} = %{EVRD}
Requires: %{_lib}absl_strings_internal%{major} = %{EVRD}
Requires: %{_lib}absl_graphcycles_internal%{major} = %{EVRD}
Requires: %{_lib}absl_strings%{major} = %{EVRD}
Requires: %{_lib}absl_hash%{major} = %{EVRD}
Requires: %{_lib}absl_symbolize%{major} = %{EVRD}
Requires: %{_lib}absl_hashtablez_sampler%{major} = %{EVRD}
Requires: %{_lib}absl_synchronization%{major} = %{EVRD}
Requires: %{_lib}absl_int128_%{major} = %{EVRD}
Requires: %{_lib}absl_throw_delegate%{major} = %{EVRD}
Requires: %{_lib}absl_leak_check_disable%{major} = %{EVRD}
Requires: %{_lib}absl_time%{major} = %{EVRD}
Requires: %{_lib}absl_leak_check%{major} = %{EVRD}
Requires: %{_lib}absl_time_zone%{major} = %{EVRD}

Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development headers for %{name}

%files -n %{devname}
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so

#---------------------------------------------------------------------------

%prep
%autosetup

%build
%cmake
%make_build

%install
%make_install -C build

#add versioning for lib's
pushd %{buildroot}%{_libdir}
for file in *.so;
do
  patchelf --set-soname $file.%{major} $file
  for f in `patchelf --print-needed $file |grep libabsl_`;
  do
  patchelf --replace-needed $f $f.%{major} $file
  done
  mv -v $file $file.%{major}
  ln -s $file.%{major} $file
done
popd

