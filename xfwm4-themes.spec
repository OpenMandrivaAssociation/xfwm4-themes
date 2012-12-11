Summary:	Additional themes for Xfwm
Name:		xfwm4-themes
Version:	4.6.0
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
Requires:	xfwm4 >= %{version}
BuildArch:	noarch
Obsoletes:	xfwm-themes

%description
A set of additional themes for the Xfwm window manager.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README TODO AUTHORS
%{_datadir}/themes/*


%changelog
* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-6mdv2011.0
+ Revision: 660752
- rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 4.6.0-5mdv2011.0
+ Revision: 615677
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-4mdv2010.1
+ Revision: 543318
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 4.6.0-3mdv2010.0
+ Revision: 446161
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349282
- rebuild whole xfce

* Fri Feb 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345493
- update to new version 4.6.0

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333833
- update to new version 4.5.99.1

* Wed Jan 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329526
- update to new version 4.5.93
- add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303459
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Thu Oct 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294492
- Xfce4.6 beta1 is landing on cooker

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-4mdv2009.0
+ Revision: 262433
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-3mdv2009.0
+ Revision: 257089
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Nov 18 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109975
- New release 4.4.2?\195?\169

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new license policy
    - use upstream tarball name as a real name
    - use upstream name

* Tue May 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 32562
- use macros
- spec file clean

* Mon Apr 23 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2008.0
+ Revision: 17708
- New release 4.4.1

