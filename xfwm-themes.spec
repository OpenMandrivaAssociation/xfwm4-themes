Summary:	Additional themes for Xfwm
Name:		xfwm-themes
Version:	4.4.1
Release:	%mkrel 2
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	xfwm4-themes-%{version}.tar.bz2
Requires:	xfwm
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A set of additional themes for the Xfwm window manager.

%prep
%setup -qn xfwm4-themes-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove galaxy theme, it sucks anyway :-)
rm -rf %{buildroot}/%{_datadir}/themes/Galaxy

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO COPYING AUTHORS
%{_datadir}/themes/*
