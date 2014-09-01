Summary:	Display I/O usage of processes in a top like UI
Name:		iotop
Version:	0.6
Release:	1
License:	GPLv2
Group:		Monitoring
Url:		http://guichaz.free.fr/iotop/
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
BuildRequires:	zlib
BuildRequires:	python-devel
Requires:	python
BuildArch:	noarch

%description
iotop is a Python program with a top like UI used to show of behalf of
which process is the I/O going on. It requires a Linux kernel 2.6.20
with TASK_IO_ACCOUNTING enabled.

%prep
%setup -q
# fix python3
sed -i 's/itervalues/values/' setup.py

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc NEWS THANKS
%{_sbindir}/%{name}
%{py_sitedir}/*
%{_mandir}/man8/*
