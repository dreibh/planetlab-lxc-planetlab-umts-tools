%define module_taglevel_varname release

%define name planetlab-umts-tools-frontend
%define version 0.6
%define release 6

Summary: UMTS tools for PlanetLab
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: Universita Federico II di Napoli for Onelab
Group: Utilities
URL: http://www.unina.it
License: GPL
Prefix: %{_prefix}

%description
Frontend part of a program that allows users of a slice to control a PPP connection over a 3G umts/hsdpa connect card and set the route entries required to use it.

%prep

%setup -q

%build
rm -rf $RPM_BUILD_ROOT
pushd frontend
make 
popd 

%install
rm -rf $RPM_BUILD_ROOT
pushd frontend
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install -D -s umts $RPM_BUILD_ROOT/usr/bin/
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-,root,root)
/usr/bin/umts
%doc AUTHORS VERSION README.User README.PI

%changelog
* Mon Jan 24 2011 Thierry Parmentelat <thierry.parmentelat@sophia.inria.fr> - planetlab-umts-tools-0.6-6
- no semantic change - just fixed specfile for git URL

* Tue Jul 06 2010 Baris Metin <Talip-Baris.Metin@sophia.inria.fr> - planetlab-umts-tools-0.6-5
- cosmetic changes from Giovanni.

* Tue Sep 30 2008 Giovanni Di Stasi <giovanni.distasi@unina.it> -
- initial revision

