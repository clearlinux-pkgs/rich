#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rich
Version  : 9.2.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/c5/5f/f0a36649beefeaa70c1086451fc936b22afb0c34879930d97d3b129aadc6/rich-9.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/5f/f0a36649beefeaa70c1086451fc936b22afb0c34879930d97d3b129aadc6/rich-9.2.0.tar.gz
Summary  : Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
Group    : Development/Tools
License  : MIT
Requires: rich-license = %{version}-%{release}
Requires: rich-python = %{version}-%{release}
Requires: rich-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Rich
[![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)
[![codecov](https://codecov.io/gh/willmcgugan/rich/branch/master/graph/badge.svg)](https://codecov.io/gh/willmcgugan/rich)
[![Rich blog](https://img.shields.io/badge/blog-rich%20news-yellowgreen)](https://www.willmcgugan.com/tag/rich/)
[![Twitter Follow](https://img.shields.io/twitter/follow/willmcgugan.svg?style=social)](https://twitter.com/willmcgugan)

%package license
Summary: license components for the rich package.
Group: Default

%description license
license components for the rich package.


%package python
Summary: python components for the rich package.
Group: Default
Requires: rich-python3 = %{version}-%{release}

%description python
python components for the rich package.


%package python3
Summary: python3 components for the rich package.
Group: Default
Requires: python3-core
Provides: pypi(rich)
Requires: pypi(colorama)
Requires: pypi(commonmark)
Requires: pypi(pygments)
Requires: pypi(typing_extensions)

%description python3
python3 components for the rich package.


%prep
%setup -q -n rich-9.2.0
cd %{_builddir}/rich-9.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605463184
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rich
cp %{_builddir}/rich-9.2.0/LICENSE %{buildroot}/usr/share/package-licenses/rich/aaba1270952b5954329751066884531f753f798f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rich/aaba1270952b5954329751066884531f753f798f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
