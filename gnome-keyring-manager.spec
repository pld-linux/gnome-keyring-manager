Summary:	Keyring manager for GNOME
Summary(pl):	Zarz±dzanie kluczami dla GNOME
Name:		gnome-keyring-manager
Version:	2.15.92
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-keyring-manager/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	1b32b61ea9b38d9c0f2c6e11c548d875
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-keyring-devel >= 0.5.2
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gnome-keyring-libs >= 0.5.2
Requires:	gtk+2 >= 2:2.10.2
Requires:	libgnomeui >= 2.15.91
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Keyring Manager is an application that manages user keyrings.

%description -l pl
GNOME Keyring Manager jest aplikacj± s³u¿±c± do zarz±dzania kluczami
u¿ytkownika.

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

#rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
%{_desktopdir}/*
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/gnome-keyring-manager.schemas
