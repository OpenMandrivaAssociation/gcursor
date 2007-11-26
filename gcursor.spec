Summary:		A little gtk program to change your Xcursor with animated preview
Name:			gcursor
Version: 		0.061
Release: 		2mdk
License:		GPL
Group:			Graphical desktop/GNOME
Source0:		%{name}-%{version}.tar.bz2
Patch1:			gcursor-0.061-desktopicon.patch.bz2
URL:			http://qballcow.nl/?s=14
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:		libglade2.0-devel libgnomeui2-devel perl-XML-Parser 
Requires:		cursor_themes

%description
A little gtk program to change youre Xcursor with anitmated preview.

This program only works with gnome 2.4 and up.
It sets a gconf key that is used by gnome's session manager.
You also need to log in gnome again to make the changes (hopefully 
this will change in gnome).
 
%prep
%setup -q
%patch1 -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL TODO
%{_bindir}/gcursor
%{_datadir}/applications/gcursor.desktop
%{_datadir}/gcursor/gcursor.glade

