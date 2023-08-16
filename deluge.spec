Summary:	A Python BitTorrent client with support for UPnP and DHT
Summary(pl.UTF-8):	Klient BitTorrenta napisany w Pythonie ze wspraciem dla UPnP i DHT
Name:		deluge
Version:	2.1.1
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	https://ftp.osuosl.org/pub/deluge/source/2.1/%{name}-%{version}.tar.xz
# Source0-md5:	2f132a55217fd250967678c9a555bad5
URL:		http://deluge-torrent.org/
BuildRequires:	closure-compiler
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	/bin/sh
Requires:	GConf2
Requires:	hicolor-icon-theme
Requires:	libappindicator-gtk3
# for svg pixbuf loader
Requires:	librsvg
Requires:	python3-Mako
Requires:	python3-pyasn1
Requires:	python3-twisted >= 17.1
Requires:	python3-chardet
Requires:	python3-dbus
Requires:	python3-distro
Requires:	python3-libtorrent-rasterbar >= 1.2.0
Requires:	python3-ifaddr
Requires:	python3-pillow
Requires:	python3-pyOpenSSL
Requires:	python3-pycairo
Requires:	python3-pygobject3
Requires:	python3-pyxdg
Requires:	python3-service_identity
Requires:	python3-setproctitle
Requires:	python3-setuptools
Requires:	python3-zope.interface
Requires:	xdg-utils
Suggests:	GeoIP-db-Country
Suggests:	libnotify
Suggests:	python3-pygame
BuildArch:	noarch
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
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install --skip-build

# not supported in glibc (as for 2.14-15)
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{name}/i18n/{pms,lb,iu,te,tlh,ur}

# move lang files into %{_localedir}, find_lang does not work on
# this. Looks really ugly, if you know a better way please do use it :)
install -d $RPM_BUILD_ROOT%{_localedir}
for f in $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{name}/i18n/[a-z]* ; do
	[ -d "$f" ] || continue
	%{__mv} $f $RPM_BUILD_ROOT%{_localedir}
	ln -sr $RPM_BUILD_ROOT%{_localedir}/$(basename $f) $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{name}/i18n/
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/deluge
%attr(755,root,root) %{_bindir}/deluge-console
%attr(755,root,root) %{_bindir}/deluge-gtk
%attr(755,root,root) %{_bindir}/deluge-web
%attr(755,root,root) %{_bindir}/deluged
%dir %{py3_sitescriptdir}/%{name}
%dir %{py3_sitescriptdir}/%{name}/core
%dir %{py3_sitescriptdir}/%{name}/i18n
%dir %{py3_sitescriptdir}/%{name}/plugins
%dir %{py3_sitescriptdir}/%{name}/ui
%dir %{py3_sitescriptdir}/%{name}/ui/console
%dir %{py3_sitescriptdir}/%{name}/ui/console/cmdline
%dir %{py3_sitescriptdir}/%{name}/ui/console/cmdline/commands
%dir %{py3_sitescriptdir}/%{name}/ui/console/modes
%dir %{py3_sitescriptdir}/%{name}/ui/console/modes/preferences
%dir %{py3_sitescriptdir}/%{name}/ui/console/modes/torrentlist
%dir %{py3_sitescriptdir}/%{name}/ui/console/utils
%dir %{py3_sitescriptdir}/%{name}/ui/console/widgets
%dir %{py3_sitescriptdir}/%{name}/ui/data
%dir %{py3_sitescriptdir}/%{name}/ui/data/pixmaps
%dir %{py3_sitescriptdir}/%{name}/ui/data/pixmaps/flags
%dir %{py3_sitescriptdir}/%{name}/ui/gtk3
%dir %{py3_sitescriptdir}/%{name}/ui/gtk3/glade
%dir %{py3_sitescriptdir}/%{name}/ui/web
%{py3_sitescriptdir}/%{name}/__pycache__
%{py3_sitescriptdir}/%{name}/*.py
%{py3_sitescriptdir}/%{name}/core/__pycache__
%{py3_sitescriptdir}/%{name}/core/*.py
%{py3_sitescriptdir}/%{name}/i18n/__pycache__
%{py3_sitescriptdir}/%{name}/i18n/*.py
%{py3_sitescriptdir}/%{name}/i18n/[a-z][a-z]
%{py3_sitescriptdir}/%{name}/i18n/[a-z][a-z][a-z]
%{py3_sitescriptdir}/%{name}/i18n/[a-z][a-z]_[A-Z][A-Z]
%{py3_sitescriptdir}/%{name}/plugins/__pycache__
%{py3_sitescriptdir}/%{name}/plugins/*.py
%{py3_sitescriptdir}/%{name}/plugins/*.egg
%{py3_sitescriptdir}/%{name}/ui/__pycache__
%{py3_sitescriptdir}/%{name}/ui/*.py
%{py3_sitescriptdir}/%{name}/ui/console/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/*.py
%{py3_sitescriptdir}/%{name}/ui/console/cmdline/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/cmdline/*.py
%{py3_sitescriptdir}/%{name}/ui/console/cmdline/commands/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/cmdline/commands/*.py
%{py3_sitescriptdir}/%{name}/ui/console/modes/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/modes/*.py
%{py3_sitescriptdir}/%{name}/ui/console/modes/preferences/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/modes/preferences/*.py
%{py3_sitescriptdir}/%{name}/ui/console/modes/torrentlist/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/modes/torrentlist/*.py
%{py3_sitescriptdir}/%{name}/ui/console/utils/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/utils/*.py
%{py3_sitescriptdir}/%{name}/ui/console/widgets/__pycache__
%{py3_sitescriptdir}/%{name}/ui/console/widgets/*.py
%{py3_sitescriptdir}/%{name}/ui/data/pixmaps/*.gif
%{py3_sitescriptdir}/%{name}/ui/data/pixmaps/*.ico
%{py3_sitescriptdir}/%{name}/ui/data/pixmaps/*.png
%{py3_sitescriptdir}/%{name}/ui/data/pixmaps/*.svg
%{py3_sitescriptdir}/%{name}/ui/data/pixmaps/flags/*.png
%{py3_sitescriptdir}/%{name}/ui/gtk3/__pycache__
%{py3_sitescriptdir}/%{name}/ui/gtk3/*.py
%{py3_sitescriptdir}/%{name}/ui/gtk3/glade/*.ui
%{py3_sitescriptdir}/%{name}/ui/web/__pycache__
%{py3_sitescriptdir}/%{name}/ui/web/*.py
%{py3_sitescriptdir}/%{name}/ui/web/css
%{py3_sitescriptdir}/%{name}/ui/web/icons
%{py3_sitescriptdir}/%{name}/ui/web/images
%{py3_sitescriptdir}/%{name}/ui/web/index.html
%{py3_sitescriptdir}/%{name}/ui/web/js
%{py3_sitescriptdir}/%{name}/ui/web/render
%{py3_sitescriptdir}/%{name}/ui/web/themes
%{py3_sitescriptdir}/%{name}-*-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
/usr/share/appdata/deluge.appdata.xml
%{_iconsdir}/hicolor/*x*/apps/deluge.png
%{_iconsdir}/hicolor/*x*/apps/deluge-panel.png
%{_iconsdir}/hicolor/scalable/apps/deluge.svg
%{_mandir}/man1/deluge.1*
%{_mandir}/man1/deluged.1*
%{_mandir}/man1/deluge-console.1*
%{_mandir}/man1/deluge-gtk.1*
%{_mandir}/man1/deluge-web.1*
