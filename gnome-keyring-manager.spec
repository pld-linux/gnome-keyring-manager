#
# TODO:
# - should there be R: libgnomeui >= 2.17?
#
Summary:	Keyring manager for GNOME
Summary(pl):	Zarządzanie kluczami dla GNOME
Name:		gnome-keyring-manager
Version:	2.17.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-keyring-manager/2.17/%{name}-%{version}.tar.bz2
# Source0-md5:	8dc9c133ccdfb2729898a05afa177a0d
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gnome-keyring-devel >= 0.6.0
BuildRequires:	gtk+2-devel >= 2:2.10.3
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gnome-keyring-libs >= 0.6.0
Requires:	gtk+2 >= 2:2.10.3
Requires:	libgnomeui >= 2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Keyring Manager is an application that manages user keyrings.

%description -l pl
GNOME Keyring Manager jest aplikacją służącą do zarządzania kluczami
użytkownika.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_prepare}
%{__aclocal}
%{__automake}
%{__autoconf}
%{__gnome_doc_common}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}  --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-keyring-manager.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gnome-keyring-manager.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/gnome-keyring-manager.schemas
