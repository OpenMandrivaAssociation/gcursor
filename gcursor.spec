Summary:		A little gtk program to change your Xcursor with animated preview
Name:			gcursor
Version: 		0.061
Release: 		 %mkrel 6
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.061-6mdv2011.0
+ Revision: 618432
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.061-5mdv2010.0
+ Revision: 429184
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.061-4mdv2009.0
+ Revision: 245779
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.061-2mdv2008.1
+ Revision: 125531
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import gcursor


* Mon Jun 27 2005 Pascal Terjan <pterjan@mandriva.org> 0.061-2mdk
- BuildRequires perl-XML-Parser for embedded intltool

* Sun May 08 2005 Pascal Terjan <pterjan@mandriva.org> 0.061-1mdk
- Don't explicitly Requires libgtk+2.0
- BuildRequires libglade2.0-devel and libgnomeui2-devel
- Don't BuildRequires libgtk+2.0-devel, it will be implied
- Don't ship NEWS and README as they are empty
- From Tigrux <tigrux@ximian.com>
 - First rpm for Mandriva
