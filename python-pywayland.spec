%undefine _debugsource_packages
Name:           python-pywayland
Version:        0.4.18
Release:        3
Summary:        Python bindings for the libwayland library written in pure Python
License:        Apache-2.0 AND ISC AND NTP
URL:            https://github.com/flacjacket/pywayland/
Source:         https://files.pythonhosted.org/packages/source/p/pywayland/pywayland-%{version}.tar.gz

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cffi)
Requires:		python%{pyver}dist(cffi)

%description
PyWayland provides a wrapper to the libwayland library using the CFFI library
to provide access to the Wayland library calls and written in pure Python.}

%prep
%autosetup -n pywayland-%{version} -p1

%build
#cd pywayland
#python ffi_build.py
#cd ..
python ./pywayland/ffi_build.py
python -m pywayland.scanner --with-protocols
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{_bindir}/pywayland-scanner
%{python_sitelib}/pywayland-%{version}.dist-info
%{python_sitelib}/pywayland/
