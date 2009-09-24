Summary:	Display I/O usage of processes in a top like UI
Name:		iotop
Version:	0.3.2
Release:	%mkrel 1
License:	GPLv2
Group:		Monitoring
Url:		http://guichaz.free.fr/iotop/
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
BuildRequires:	zlib
%py_requires -d
Requires:	python
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
iotop is a Python program with a top like UI used to show of behalf of
which process is the I/O going on. It requires a Linux kernel 2.6.20
with TASK_IO_ACCOUNTING enabled.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS THANKS
%{_bindir}/%{name}
%{py_sitedir}/*
%{_mandir}/man1/*
