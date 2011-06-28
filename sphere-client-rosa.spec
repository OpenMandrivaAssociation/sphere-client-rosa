%define name    sphere-client-rosa
%define version 1
%define release 0
%define buildroot %{_tmppath}/%{name}-buildroot

BuildRoot:      %{buildroot}
Summary:        sphere-client-rosa
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL-3
Group:          System/Configuration
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  qxmlrpc
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
cp sphere-client $RPM_BUILD_ROOT/usr/bin
cp sphere-client.conf $RPM_BUILD_ROOT/etc
%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(0755,root,root)
/usr/bin/*
/etc/*