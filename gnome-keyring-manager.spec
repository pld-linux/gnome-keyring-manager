Summary:	Keyring manager for GNOME
Summary(pl):	Zarz±dzanie kluczami dla GNOME
Name:		gnome-keyring-manager
Version:	0.0.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-keyring-manager/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	3f6e2f3ebe973317eeface0b8ffff090
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	gnome-keyring-devel >= 0.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeui-devel >= 2.6.0
Requires(post):	GConf2
Requires:	gtk+2 >= 2:2.4.4
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
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_desktopdir}/*
