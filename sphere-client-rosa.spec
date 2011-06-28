%define name    sphere-client-rosa
%define version 1
%define release 1
%define buildroot %{_tmppath}/%{name}-buildroot

BuildRoot:      %{buildroot}
Summary:        sphere-client-rosa
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL-3
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
Source1:        sphere-client.desktop
BuildRequires:  qxmlrpc
BuildRequires: qt4-devel

%description
sphere-client-rosa
%prep
%setup -q
%build
qmake
make 
%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/etc/
mkdir -p $RPM_BUILD_ROOT/usr/share/autostart
cp sphere-client $RPM_BUILD_ROOT/usr/bin
cp sphere-client.conf $RPM_BUILD_ROOT/etc
cp %SOURCE1 $RPM_BUILD_ROOT/usr/share/autostart/

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(0755,root,root)
/usr/bin/*
/etc/*
/usr/share/autostart/