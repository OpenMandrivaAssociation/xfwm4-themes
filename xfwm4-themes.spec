Summary:	Additional themes for Xfwm
Name:		xfwm4-themes
Version:	4.10.0
Release:	2
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
