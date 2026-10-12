Summary:	Display I/O usage of processes in a top like UI
Name:		iotop
Version:	0.6
Release:	7
License:	GPLv2
Group:		Monitoring
Url:		https://guichaz.free.fr/iotop/
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
BuildRequires:	zlib
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python
BuildArch:	noarch

%description
iotop is a Python program with a top like UI used to show of behalf of
which process is the I/O going on. It requires a Linux kernel 2.6.20
with TASK_IO_ACCOUNTING enabled.

%prep
%setup -q
# setuptools 84 has no distutils install schemes. Put the script in sbin below.
python - << 'PY'
from pathlib import Path
lines = Path("setup.py").read_text().splitlines(True)
out = []
skip = False
for line in lines:
    if line.startswith("from distutils.core import setup"):
        out.append("from setuptools import setup\n")
        continue
    if line.startswith("from distutils.command import install"):
        skip = True
        continue
    if skip:
        if line.startswith("setup("):
            skip = False
            out.append(line)
        continue
    out.append(line)
Path("setup.py").write_text("".join(out))
PY

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/iotop %{buildroot}%{_sbindir}/iotop

%files
%doc NEWS THANKS
%{_sbindir}/%{name}
%{py_sitedir}/*
%{_mandir}/man8/*
