Summary:	Display I/O usage of processes in a top like UI
Name:		iotop
Version:	0.4.4
Release:	%mkrel 1
License:	GPLv2
Group:		Monitoring
Url:		http://guichaz.free.fr/iotop/
Source0:	http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
BuildRequires:	zlib
%py_requires -d
Requires:	python
BuildArch:	noarch

%description
iotop is a Python program with a top like UI used to show of behalf of
which process is the I/O going on. It requires a Linux kernel 2.6.20
with TASK_IO_ACCOUNTING enabled.

%prep
%setup -q

%build
python setup.py build

%install
%__rm -rf %{buildroot}

python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS THANKS
%{_bindir}/%{name}
%{py_sitedir}/*
%{_mandir}/man1/*


%changelog
* Tue Feb 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.4-1
+ Revision: 773948
- New version 0.4.4

* Sat Apr 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.3-1
+ Revision: 649864
- update to new version 0.4.3

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.4.1-2mdv2011.0
+ Revision: 590134
- rebuild for python 2.7

* Sun Jul 11 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 550958
- update to new version 0.4.1

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 0.4-1mdv2010.1
+ Revision: 493779
- update to new version 0.4

* Thu Sep 24 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.2-1mdv2010.0
+ Revision: 448397
- update to new version 0.3.2

* Thu Jun 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.1-1mdv2010.0
+ Revision: 385178
- update to new version 0.3.1

* Sun May 17 2009 trem <trem@mandriva.org> 0.3-1mdv2010.0
+ Revision: 376628
- update to 0.3

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.2.1-4mdv2009.1
+ Revision: 326081
- rebuild
- rebuild

* Tue Jan 06 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.1-2mdv2009.1
+ Revision: 325317
- Rebuild for new python

* Sun Jul 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 250582
- add missing buildrequires on zlib
- update to new version 0.2.1
- correct the url and source
- fix mixture of tabs and spaces
- spec file clean

* Fri Jul 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0-3mdv2009.0
+ Revision: 238199
- spec cleanup

  + Michael Scherer <misc@mandriva.org>
    - add missing requires on python, as found by guillomovitch

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Dec 18 2007 Olivier Blin <blino@mandriva.org> 0-1mdv2008.1
+ Revision: 132091
- build as noarch
- initial iotop package
- create iotop

