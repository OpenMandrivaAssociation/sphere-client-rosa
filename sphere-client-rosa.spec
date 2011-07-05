Summary:        sphere-client-rosa
Name:           sphere-client-rosa
Version:        1
Release:        4
License:        GPLv3
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
Source1:        sphere-client.desktop
BuildRequires:  qxmlrpc
BuildRequires:  qt4-devel

%files
%defattr(0755,root,root)
%{_bindir}/sphere-client
%{_sysconfdir}/sphere-client.conf
%{_datadir}/autostart/sphere-client.desktop

#--------------------------------------------------------------------

%description
sphere-client-rosa

%prep
%setup -q

%build
%qmake_qt4
%make 

%install
mkdir -p %buildroot%{_bindir}
mkdir -p %buildroot%{_sysconfdir}
mkdir -p %buildroot%{_datadir}/autostart
cp sphere-client %buildroot%{_bindir}
cp sphere-client.conf %buildroot%{_sysconfdir}
cp %SOURCE1 %buildroot%{_datadir}/autostart/

