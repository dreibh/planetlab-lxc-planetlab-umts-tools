%define module_taglevel_varname release

%define name planetlab-umts-tools-backend
%define version 0.6
%define release 6

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
rm -rf $RPM_BUILD_ROOT
pushd backend
mkdir -p $RPM_BUILD_ROOT
make clean
make install prefix=$RPM_BUILD_ROOT
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/udevadm control reload_rules
sleep 1
/sbin/udevtrigger
#/bin/sleep 2
#/sbin/chkconfig umts on
/sbin/service vsys restart
/etc/rc.d/init.d/umts start

%preun
#/sbin/chkconfig umts off

%files
/vsys/umtsd
/usr/lib/umts_functions
/etc/udev/rules.d/96-umts-tools.rules
/etc/rc.d/init.d/umts


%defattr(-,root,root)
%doc AUTHORS TODO

%changelog
* Mon Jan 24 2011 Thierry Parmentelat <thierry.parmentelat@sophia.inria.fr> - planetlab-umts-tools-0.6-6
- no semantic change - just fixed specfile for git URL

* Tue Jul 06 2010 Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - planetlab-umts-tools-0.6-5
- cosmetic changes from Giovanni.

* Tue Sep 30 2008 Giovanni Di Stasi <giovanni.distasi@unina.it> -
- initial revision
