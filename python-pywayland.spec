Name:           python-pywayland
Version:        0.4.18
Release:        1
Summary:        Python bindings for the libwayland library written in pure Python
License:        Apache-2.0 AND ISC AND NTP
URL:            https://github.com/flacjacket/pywayland/
Source:         https://files.pythonhosted.org/packages/source/p/pywayland/pywayland-%{version}.tar.gz

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(python3)
BuildSystem: Python

%description
PyWayland provides a wrapper to the libwayland library using the CFFI library
to provide access to the Wayland library calls and written in pure Python.}


%files
%license LICENSE
%doc README.rst
%{_bindir}/pywayland-scanner
