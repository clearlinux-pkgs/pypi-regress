#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v2
# autospec commit: e661f3a
#
Name     : pypi-regress
Version  : 0.4.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/4b/05/6d4bc9557e4a999368d42dc9f4b166db0a5727a20c92b949a6254669dfd0/regress-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4b/05/6d4bc9557e4a999368d42dc9f4b166db0a5727a20c92b949a6254669dfd0/regress-0.4.2.tar.gz
Source1  : http://localhost/cgit/vendor/pypi-regress/snapshot/pypi-regress-2023-11-29-00-22-51.tar.xz
Summary  : Python bindings to Rust's regress ECMA regular expressions library
Group    : Development/Tools
License  : Apache-2.0 MIT Unicode-DFS-2016 Unlicense
Requires: pypi-regress-license = %{version}-%{release}
Requires: pypi-regress-python = %{version}-%{release}
Requires: pypi-regress-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(maturin)
BuildRequires : pypi-maturin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===========
``regress``
===========
|PyPI| |Pythons| |CI|
.. |PyPI| image:: https://img.shields.io/pypi/v/regress.svg
:alt: PyPI version
:target: https://pypi.org/project/regress/

%package license
Summary: license components for the pypi-regress package.
Group: Default

%description license
license components for the pypi-regress package.


%package python
Summary: python components for the pypi-regress package.
Group: Default
Requires: pypi-regress-python3 = %{version}-%{release}

%description python
python components for the pypi-regress package.


%package python3
Summary: python3 components for the pypi-regress package.
Group: Default
Requires: python3-core
Provides: pypi(regress)

%description python3
python3 components for the pypi-regress package.


%prep
%setup -q -n regress-0.4.2
cd %{_builddir}
tar xf %{_sourcedir}/pypi-regress-2023-11-29-00-22-51.tar.xz
cd %{_builddir}/regress-0.4.2
mkdir -p ./vendor
cp -r %{_builddir}/pypi-regress-2023-11-29-00-22-51/* %{_builddir}/regress-0.4.2/./vendor
mkdir -p .cargo
echo '[source.crates-io]' >> .cargo/config.toml
echo 'replace-with = "vendored-sources"' >> .cargo/config.toml
echo '[source.vendored-sources]' >> .cargo/config.toml
echo 'directory = "vendor"' >> .cargo/config.toml
pushd ..
cp -a regress-0.4.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701219170
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-regress
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/ahash/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/ahash/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/2646b6d2453275031022ab245a3a6d5da4ba80b2 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/e6d32072ef5f584a805b429ecbd4eec428316dde || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/9f3c36d2b7d381d9cf382a00166f3fbd06783636 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/3b042d3d971924ec0296687efd50dbe08b734976 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/hashbrown/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/hashbrown/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/c9c1c33aee599ebfdfb0bc2aed9ea082d9e3173a || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/indoc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/indoc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/36d69bcb88153a640740000efe933b009420ce7e || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/lock_api/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/lock_api/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/memchr/COPYING %{buildroot}/usr/share/package-licenses/pypi-regress/dd445710e6e4caccc4f8a587a130eaeebe83f6f6 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/memchr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/4c8990add9180fc59efa5b0d8faf643c9709501e || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/memchr/UNLICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/memoffset/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/02bf11a87b9bbacedf2fcf4856af3b933faef82e || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/once_cell/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/once_cell/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/parking_lot/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/parking_lot/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/parking_lot_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/parking_lot_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/pyo3-build-config/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/pyo3-macros-backend/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/pyo3-macros/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/pyo3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/5bb5828e544f63bd76c1b7112981a1ad86ae77f9 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/a00165152c82ea55b9fc254890dc8860c25e3bb6 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/regress/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/c43025bca3f7d7f985c06efcea467aecfaf9ccf1 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/regress/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/f48aaaf87a9548b8a5842dc9f34c846aee9c3420 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/scopeguard/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/scopeguard/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/f498d95a48889a0b1432e420e6754881eff1d593 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/smallvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/smallvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/c61640f6c218caf86d1b8072e09668a8362dba04 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/target-lexicon/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/f137043e018f2024e0414a9153ea728c203ae8e5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/unicode-ident/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/unicode-ident/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/unicode-ident/LICENSE-UNICODE %{buildroot}/usr/share/package-licenses/pypi-regress/583a5eebcf6119730bd96922e8a0faecf7faf720 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/unindent/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/unindent/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/version_check/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/version_check/LICENSE-MIT %{buildroot}/usr/share/package-licenses/pypi-regress/cfcb552ef0afbe7ccb4128891c0de00685988a4b || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows-sys/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows-sys/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows-targets/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows-targets/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_aarch64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_aarch64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_aarch64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_aarch64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_i686_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_i686_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_i686_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_i686_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_x86_64_gnu/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_x86_64_gnu/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_x86_64_gnullvm/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_x86_64_gnullvm/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_x86_64_msvc/license-apache-2.0 %{buildroot}/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994 || :
cp %{_builddir}/pypi-regress-2023-11-29-00-22-51/windows_x86_64_msvc/license-mit %{buildroot}/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/regress-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-regress/30a3d7eda1e8880325b611de40e44026ed5866ea || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-regress/02bf11a87b9bbacedf2fcf4856af3b933faef82e
/usr/share/package-licenses/pypi-regress/2646b6d2453275031022ab245a3a6d5da4ba80b2
/usr/share/package-licenses/pypi-regress/30a3d7eda1e8880325b611de40e44026ed5866ea
/usr/share/package-licenses/pypi-regress/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/pypi-regress/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/pypi-regress/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/pypi-regress/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/pypi-regress/583a5eebcf6119730bd96922e8a0faecf7faf720
/usr/share/package-licenses/pypi-regress/5bb5828e544f63bd76c1b7112981a1ad86ae77f9
/usr/share/package-licenses/pypi-regress/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/pypi-regress/6e5c4711bcae04967d7f5b5e01cf56ae03bebe7a
/usr/share/package-licenses/pypi-regress/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/pypi-regress/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/pypi-regress/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/pypi-regress/a3b3a65335e78bde163f84d599fa899776552994
/usr/share/package-licenses/pypi-regress/c43025bca3f7d7f985c06efcea467aecfaf9ccf1
/usr/share/package-licenses/pypi-regress/c61640f6c218caf86d1b8072e09668a8362dba04
/usr/share/package-licenses/pypi-regress/c9c1c33aee599ebfdfb0bc2aed9ea082d9e3173a
/usr/share/package-licenses/pypi-regress/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/pypi-regress/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/pypi-regress/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/pypi-regress/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/pypi-regress/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/pypi-regress/f48aaaf87a9548b8a5842dc9f34c846aee9c3420
/usr/share/package-licenses/pypi-regress/f498d95a48889a0b1432e420e6754881eff1d593
/usr/share/package-licenses/pypi-regress/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
