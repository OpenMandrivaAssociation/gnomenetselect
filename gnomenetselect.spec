%define name gnomenetselect
%define version 0.6
%define release %mkrel 9

Summary: Enhanced Mozilla launch button for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://gnomenetselect.sourceforge.net/
BuildRequires: libpanel-applet-devel
BuildRequires: libglade2.0-devel
BuildRequires: scrollkeeper
BuildRequires: libxmu-devel
Requires: webclient
Requires(post)  : scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3


%description
Gnome NetSelect gives you a button for launching a web browser, and
jumping to URL or search results.

Gnome NetSelect can use the currently highlighted text. Just highlight
some text in any application and then click on the applet to jump to
the highlighted URL, or perform a search using the highlighted text.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang gnome-netselect --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gnome-netselect.schemas > /dev/null
if [ -x %_bindir/scrollkeeper-update ]; then %_bindir/scrollkeeper-update -q || true ; fi

%preun
if [ "$1" = "0" ] ; then
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gnome-netselect.schemas > /dev/null
fi

%postun
if [ -x %_bindir/scrollkeeper-update ]; then %_bindir/scrollkeeper-update -q || true ; fi


%files -f gnome-netselect.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%_sysconfdir/gconf/schemas/gnome-netselect.schemas
%_bindir/gnome-netselect
%_libdir/bonobo/servers/Gnome_NetSelect_Factory.server
%_datadir/gnome-2.0/ui/gnome-netselect.xml
%_datadir/gnome-netselect/
%_datadir/pixmaps/gnome-netselect/
%dir %_datadir/omf/gnome-netselect
%_datadir/omf/gnome-netselect/gnome-netselect-C.omf
