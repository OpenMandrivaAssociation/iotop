Summary: Display I/O usage of processes in a top like UI
Name: iotop
Version: 0
Release: %mkrel 1
Source0: http://guichaz.free.fr/misc/iotop.py
License: GPLv2
Group: Monitoring
Url: http://guichaz.free.fr/misc/#iotop
BuildArch: noarch

%description
iotop is a Python program with a top like UI used to show of behalf of
which process is the I/O going on. It requires a Linux kernel 2.6.20
with TASK_IO_ACCOUNTING enabled.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%build

%install
rm -rf %{buildroot}
install -D -m 755 %{name}.py %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
