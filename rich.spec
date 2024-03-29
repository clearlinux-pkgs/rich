#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rich
Version  : 10.16.2
Release  : 52
URL      : https://files.pythonhosted.org/packages/74/c3/e55ebdd66540503cee29cd3bb18a90bcfd5587a0cf3680173c368be56093/rich-10.16.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/c3/e55ebdd66540503cee29cd3bb18a90bcfd5587a0cf3680173c368be56093/rich-10.16.2.tar.gz
Summary  : Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
Group    : Development/Tools
License  : MIT
Requires: rich-license = %{version}-%{release}
Requires: rich-python = %{version}-%{release}
Requires: rich-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://pypi.org/project/rich/) [![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)

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

%description python3
python3 components for the rich package.


%prep
%setup -q -n rich-10.16.2
cd %{_builddir}/rich-10.16.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641237841
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rich
cp %{_builddir}/rich-10.16.2/LICENSE %{buildroot}/usr/share/package-licenses/rich/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rich/aa95e7e0dbe72bae99f41dc862f0516da8ae35c2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
