%define module_taglevel_varname release

%define name planetlab-umts-tools-backend
%define version 0.5
%define release 3

Summary: Umts-tools for PlanetLab - backend part
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Vendor: Universita Federico II di Napoli for Onelab
Group: Utilities
URL: http://www.unina.it
License: GPL
Prefix: %{_prefix}

Requires: vsys

%description
Backend part of a program that allows users of a slice to control a PPP connection over a 3G umts/hsdpa connect card and set the route entries required to use it.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

%install
pushd backend
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make clean
make install prefix=$RPM_BUILD_ROOT
popd

%clean


%post 
/sbin/udevadm control reload_rules
/sbin/udevtrigger
/bin/sleep 2
/sbin/chkconfig umts on
/sbin/service vsys restart
/etc/rc.d/init.d/umts start

%preun
/sbin/chkconfig umts off

%files
/vsys/umts_backend
/usr/lib/umts_functions
/etc/udev/rules.d/96-umts-tools.rules
/etc/rc.d/init.d/umts

%defattr(-,root,root)
%doc backend/AUTHORS backend/TODO

%changelog
* Tue Sep 30 2008 Giovanni Di Stasi <giovanni.distasi@unina.it> -
- initial revision
