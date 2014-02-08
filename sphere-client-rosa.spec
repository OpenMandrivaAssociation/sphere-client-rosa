%define debug_package %{nil}

Summary:        Sphere-client-rosa
Name:           sphere-client-rosa
Version:        1
Release:        13
License:        GPLv3
Group:          System/Base
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  qxmlrpc-devel
BuildRequires:  qt4-devel

%files
%defattr(0755,root,root)
%{_bindir}/sphere-client
%{_sysconfdir}/sphere-client.conf
%{_bindir}/sphere-client_ru.qm
%{_bindir}/sphere-client_pt_br.qm
/usr/share/applications/sphere-client.desktop
/usr/share/icons/hicolor/128x128/apps/sphere-client.png
/usr/share/icons/hicolor/16x16/apps/sphere-client.png
/usr/share/icons/hicolor/22x22/apps/sphere-client.png
/usr/share/icons/hicolor/24x24/apps/sphere-client.png
/usr/share/icons/hicolor/32x32/apps/sphere-client.png
/usr/share/icons/hicolor/48x48/apps/sphere-client.png
/usr/share/icons/hicolor/64x64/apps/sphere-client.png

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
mkdir -p %buildroot/usr/share/applications/
mkdir -p %buildroot/usr/share/icons/hicolor/128x128/apps/
mkdir -p %buildroot/usr/share/icons/hicolor/16x16/apps/
mkdir -p %buildroot/usr/share/icons/hicolor/22x22/apps/
mkdir -p %buildroot/usr/share/icons/hicolor/24x24/apps/
mkdir -p %buildroot/usr/share/icons/hicolor/32x32/apps/
mkdir -p %buildroot/usr/share/icons/hicolor/48x48/apps/
mkdir -p %buildroot/usr/share/icons/hicolor/64x64/apps/


cp sphere-client %buildroot%{_bindir}
cp sphere-client_ru.qm %buildroot%{_bindir}
cp sphere-client_pt_br.qm %buildroot%{_bindir}
cp sphere-client.conf %buildroot%{_sysconfdir}
cp sphere-client.desktop %buildroot/usr/share/applications
cp ./icons/helpdesk_128.png %buildroot/usr/share/icons/hicolor/128x128/apps/sphere-client.png
cp ./icons/helpdesk_16.png %buildroot/usr/share/icons/hicolor/16x16/apps/sphere-client.png
cp ./icons/helpdesk_22.png %buildroot/usr/share/icons/hicolor/22x22/apps/sphere-client.png
cp ./icons/helpdesk_24.png %buildroot/usr/share/icons/hicolor/24x24/apps/sphere-client.png
cp ./icons/helpdesk_32.png %buildroot/usr/share/icons/hicolor/32x32/apps/sphere-client.png
cp ./icons/helpdesk_48.png %buildroot/usr/share/icons/hicolor/48x48/apps/sphere-client.png
cp ./icons/helpdesk_64.png %buildroot/usr/share/icons/hicolor/64x64/apps/sphere-client.png

%changelog
* Thu Aug 04 2011 Alex Burmashev <burmashev@mandriva.org> 1-7
+ Revision: 693231
- some minore bugfixes
- some minor bugfixes
- disabled autostart and changed source

* Tue Jul 05 2011 Alex Burmashev <burmashev@mandriva.org> 1-4
+ Revision: 688728
- changed helpdesk url in config

* Fri Jul 01 2011 Alex Burmashev <burmashev@mandriva.org> 1-3
+ Revision: 688419
- spec fix
- Leave KDE bug fix

* Tue Jun 28 2011 Eugeni Dodonov <eugeni@mandriva.com> 1-2
+ Revision: 687848
- Rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file

* Tue Jun 28 2011 Alex Burmashev <burmashev@mandriva.org> 1-1
+ Revision: 687680
- added autostart feature

* Tue Jun 28 2011 Alex Burmashev <burmashev@mandriva.org> 1-0
+ Revision: 687668
- buildrequires fix
- one more fix
- small spec fix
- import sphere-client-rosa

