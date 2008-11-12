#
# TODO:
# - fix building with libtorrent-rasterbar libs, for now it is
# disabled. Deluge uses its internal libtorrent module
# - lang files
#
Summary:	A Python BitTorrent client with support for UPnP and DHT
Summary(pl.UTF-8):	Klient BitTorrenta napisany w Pythonie ze wspraciem dla UPnP i DHT
Name:		deluge
Version:	1.0.5
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://download.deluge-torrent.org/source/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	24fd36978b2713212cf1ae679f8066d5
Patch0:		%{name}-libtorrent.patch
URL:		http://deluge-torrent.org/
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	/bin/sh
Requires:	hicolor-icon-theme
Requires:	python-dbus
Requires:	python-gnome-extras-mozilla
Requires:	python-pygtk-glade
Requires:	python-pyxdg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deluge is a new BitTorrent client, created using Python and GTK+. It
is intended to bring a native, full-featured client to Linux GTK+
desktop environments such as GNOME and XFCE. It supports features such
as DHT (Distributed Hash Tables) and UPnP (Universal Plug-n-Play) that
allow one to more easily share BitTorrent data even from behind a
router with virtually zero configuration of port-forwarding.

%description -l pl.UTF-8
Deluge to nowy klient BitTorrenta stworzony przy użyciu Pythona i
GTK+. Jego celem jest dostarczenie natywnego, w pełni funkcjonalnego
klienta dla środowisk GTK+ pod Linuksem, takich jak GNOME czy XFCE.
Obsługuje m.in. DHT (Distributed Hash Tables) i UPnP (Universal
Plug-n-Play), co pozwala łatwiej współdzielić dane BitTorrenta nawet
zza routera praktycznie bez konfiguracji przekierowywania portów.

%prep
%setup -q
%patch0 -p1

%build
%ifarch %{x8664} ppc64 sparc64
	CFLAGS="%{rpmcflags} -DAMD64" %{__python} setup.py build
%else
	CFLAGS="%{rpmcflags}" %{__python} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

#%%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}d
%dir %{py_sitedir}/%{name}
%dir %{py_sitedir}/%{name}/core
%dir %{py_sitedir}/%{name}/data
%dir %{py_sitedir}/%{name}/data/pixmaps
%dir %{py_sitedir}/%{name}/data/pixmaps/flags
%dir %{py_sitedir}/%{name}/plugins
%dir %{py_sitedir}/%{name}/ui
%dir %{py_sitedir}/%{name}/ui/gtkui
%dir %{py_sitedir}/%{name}/ui/gtkui/glade
%dir %{py_sitedir}/%{name}/ui/null
%dir %{py_sitedir}/%{name}/ui/webui
%dir %{py_sitedir}/%{name}/ui/webui/lib
%dir %{py_sitedir}/%{name}/ui/webui/lib/newforms_portable
%dir %{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/django
%dir %{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/django/core
%dir %{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/django/utils
%dir %{py_sitedir}/%{name}/ui/webui/lib/webpy022
%dir %{py_sitedir}/%{name}/ui/webui/lib/webpy022/wsgiserver
%dir %{py_sitedir}/%{name}/ui/webui/scripts
%dir %{py_sitedir}/%{name}/ui/webui/static
%dir %{py_sitedir}/%{name}/ui/webui/static/images
%dir %{py_sitedir}/%{name}/ui/webui/static/images/tango
%dir %{py_sitedir}/%{name}/ui/webui/templates
%dir %{py_sitedir}/%{name}/ui/webui/templates/classic
%dir %{py_sitedir}/%{name}/ui/webui/templates/white
%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}/core/*.py[co]
%{py_sitedir}/%{name}/data/GeoIP.dat
%{py_sitedir}/%{name}/data/revision
%{py_sitedir}/%{name}/data/pixmaps/*.ico
%{py_sitedir}/%{name}/data/pixmaps/*.png
%{py_sitedir}/%{name}/data/pixmaps/*.svg
%{py_sitedir}/%{name}/data/pixmaps/flags/*.png
%{py_sitedir}/%{name}/plugins/*.py[co]
%{py_sitedir}/%{name}/ui/*.py[co]
%{py_sitedir}/%{name}/ui/gtkui/*.py[co]
%{py_sitedir}/%{name}/ui/gtkui/glade/*.glade
%{py_sitedir}/%{name}/ui/null/*.py[co]
%{py_sitedir}/%{name}/ui/webui/LICENSE
%{py_sitedir}/%{name}/ui/webui/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/django/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/django/core/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/newforms_portable/django/utils/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/webpy022/*.py[co]
%{py_sitedir}/%{name}/ui/webui/lib/webpy022/wsgiserver/*.py[co]
%{py_sitedir}/%{name}/ui/webui/scripts/*
%{py_sitedir}/%{name}/ui/webui/static/*.css
%{py_sitedir}/%{name}/ui/webui/static/*.js
%{py_sitedir}/%{name}/ui/webui/static/images/*.gif
%{py_sitedir}/%{name}/ui/webui/static/images/*.jpg
%{py_sitedir}/%{name}/ui/webui/static/images/*.png
%{py_sitedir}/%{name}/ui/webui/static/images/tango/*.png
%{py_sitedir}/%{name}/ui/webui/templates/classic/*.cfg
%{py_sitedir}/%{name}/ui/webui/templates/classic/*.html
%{py_sitedir}/%{name}/ui/webui/templates/classic/*.txt
%{py_sitedir}/%{name}/ui/webui/templates/white/*.cfg
%{py_sitedir}/%{name}/ui/webui/templates/white/*.css
%{py_sitedir}/%{name}/ui/webui/templates/white/*.html
%{py_sitedir}/%{name}-%{version}-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/deluge.png
%{_iconsdir}/hicolor/22x22/apps/deluge.png
%{_iconsdir}/hicolor/24x24/apps/deluge.png
%{_iconsdir}/hicolor/32x32/apps/deluge.png
%{_iconsdir}/hicolor/36x36/apps/deluge.png
%{_iconsdir}/hicolor/48x48/apps/deluge.png
%{_iconsdir}/hicolor/64x64/apps/deluge.png
%{_iconsdir}/hicolor/72x72/apps/deluge.png
%{_iconsdir}/hicolor/96x96/apps/deluge.png
%{_iconsdir}/hicolor/128x128/apps/deluge.png
%{_iconsdir}/hicolor/192x192/apps/deluge.png
#{_iconsdir}/hicolor/256x256/apps/deluge.png
