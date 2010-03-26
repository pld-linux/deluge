Summary:	A Python BitTorrent client with support for UPnP and DHT
Summary(pl.UTF-8):	Klient BitTorrenta napisany w Pythonie ze wspraciem dla UPnP i DHT
Name:		deluge
Version:	1.2.2
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	http://download.deluge-torrent.org/source/%{name}-%{version}.tar.bz2
# Source0-md5:	535f65ef9854073189c9fb604a673c9f
URL:		http://deluge-torrent.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-libtorrent-rasterbar
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	/bin/sh
Requires:	hicolor-icon-theme
# for svg pixbuf loader
Requires:	librsvg
Requires:	python-Mako
Requires:	python-TwistedCore >= 8.1
Requires:	python-TwistedWeb >= 8.1
Requires:	python-chardet
Requires:	python-dbus
Requires:	python-libtorrent-rasterbar >= 0.14.9
Requires:	python-pyOpenSSL
Requires:	python-pygame
Requires:	python-pygtk-glade >= 2:2.12
Requires:	python-pygtk-gtk >= 2:2.12
Requires:	python-pynotify
Requires:	python-pyxdg
Requires:	python-setuptools
Requires:	xdg-utils
Suggests:	GeoIP-db-Country
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

%build
%ifarch %{x8664} ppc64 sparc64
	CFLAGS="%{rpmcflags} -DAMD64" %{__python} setup.py build
%else
	CFLAGS="%{rpmcflags}" %{__python} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# move lang files into %{_datadir}/locale, find_lang does not work on
# this. Looks really ugly, if you know a better way please do use it :)
install -d $RPM_BUILD_ROOT%{_localedir}
mv -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/i18n/* $RPM_BUILD_ROOT%{_localedir}
# clean *.py files from the package, macro doesn't catch those
find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name} -name '*.py' -exec %{__rm} {} \;

# unsupported(?)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/iu
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pms
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/si

%{__rm} $RPM_BUILD_ROOT%{_localedir}/deluge.pot

# Move svg icon to proper place
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps
mv -f $RPM_BUILD_ROOT%{_iconsdir}/scalable/apps/deluge.svg $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/deluge
%attr(755,root,root) %{_bindir}/deluge-console
%attr(755,root,root) %{_bindir}/deluge-gtk
%attr(755,root,root) %{_bindir}/deluge-web
%attr(755,root,root) %{_bindir}/deluged
%{_pixmapsdir}/%{name}.xpm
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/core
%dir %{py_sitescriptdir}/%{name}/data
%dir %{py_sitescriptdir}/%{name}/data/pixmaps
%dir %{py_sitescriptdir}/%{name}/data/pixmaps/flags
%dir %{py_sitescriptdir}/%{name}/plugins
%dir %{py_sitescriptdir}/%{name}/ui
%dir %{py_sitescriptdir}/%{name}/ui/console
%dir %{py_sitescriptdir}/%{name}/ui/console/commands
%dir %{py_sitescriptdir}/%{name}/ui/gtkui
%dir %{py_sitescriptdir}/%{name}/ui/gtkui/glade
%dir %{py_sitescriptdir}/%{name}/ui/web
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/core/*.py[co]
%{py_sitescriptdir}/%{name}/data/pixmaps/*.ico
%{py_sitescriptdir}/%{name}/data/pixmaps/*.png
%{py_sitescriptdir}/%{name}/data/pixmaps/*.svg
%{py_sitescriptdir}/%{name}/data/pixmaps/flags/*.png
%{py_sitescriptdir}/%{name}/plugins/*.py[co]
%{py_sitescriptdir}/%{name}/plugins/*.egg
%{py_sitescriptdir}/%{name}/ui/*.py[co]
%{py_sitescriptdir}/%{name}/ui/console/*.py[co]
%{py_sitescriptdir}/%{name}/ui/console/commands/*.py[co]
%{py_sitescriptdir}/%{name}/ui/gtkui/*.py[co]
%{py_sitescriptdir}/%{name}/ui/gtkui/glade/*.glade
%{py_sitescriptdir}/%{name}/ui/web/*.js
%{py_sitescriptdir}/%{name}/ui/web/*.py[co]
%{py_sitescriptdir}/%{name}/ui/web/css
%{py_sitescriptdir}/%{name}/ui/web/icons
%{py_sitescriptdir}/%{name}/ui/web/images
%{py_sitescriptdir}/%{name}/ui/web/index.html
%{py_sitescriptdir}/%{name}/ui/web/js
%{py_sitescriptdir}/%{name}/ui/web/render
%{py_sitescriptdir}/%{name}/ui/web/themes
%{py_sitescriptdir}/%{name}-*-py*.egg-info
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
%{_iconsdir}/hicolor/256x256/apps/deluge.png
%{_iconsdir}/hicolor/scalable/apps/deluge.svg
%{_mandir}/man1/deluge.1*
%{_mandir}/man1/deluged.1*
%{_mandir}/man1/deluge-console.1*
%{_mandir}/man1/deluge-gtk.1*
%{_mandir}/man1/deluge-web.1*
