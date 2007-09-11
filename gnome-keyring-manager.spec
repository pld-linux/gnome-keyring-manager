Summary:	Keyring manager for GNOME
Summary(pl.UTF-8):	Zarządzanie kluczami dla GNOME
Name:		gnome-keyring-manager
Version:	2.19.92
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-keyring-manager/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	162105ae1e4021eab4c613a4ca7e6bb9
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	gnome-keyring-devel >= 2.19.91
BuildRequires:	gtk+2-devel >= 2:2.10.14
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	gnome-keyring-libs >= 2.19.91
Requires:	gtk+2 >= 2:2.10.14
Requires:	libgnomeui >= 2.19.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Keyring Manager is an application that manages user keyrings.

%description -l pl.UTF-8
GNOME Keyring Manager jest aplikacją służącą do zarządzania kluczami
użytkownika.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_prepare}
%{__glib_gettextize}
%{__intltoolize}
%{__intltoolize}
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
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-C.omf
%lang(ca) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-ca.omf
%lang(da) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-da.omf
%lang(en_GB) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-en_GB.omf
%lang(es) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-es.omf
%lang(fr) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-fr.omf
%lang(oc) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-oc.omf
%lang(sv) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-sv.omf
%lang(uk) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-uk.omf
%lang(vi) %{_omf_dest_dir}/gnome-keyring-manager/gnome-keyring-manager-vi.omf
%{_sysconfdir}/gconf/schemas/gnome-keyring-manager.schemas
