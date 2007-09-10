Summary:	A Python BitTorrent client with support for UPnP and DHT
Summary(pl.UTF-8):	Klient BitTorrenta napisany w Pythonie ze wspraciem dla UPnP i DHT
Name:		deluge
Version:	0.5.5
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.deluge-torrent.org/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	76c1f8110aef4131d2bc83a7da957c6a
#Source1:	%{name}-fixed-setup.py
Patch0:		%{name}-pld.patch
Patch1:		%{name}-pyc.patch
URL:		http://deluge-torrent.org/
BuildRequires:	boost-program_options-devel
BuildRequires:	boost-regex-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rb_libtorrent-devel
BuildRequires:	rpm-pythonprov
Requires:	/bin/sh
Requires:	python-dbus
Requires:	python-pygtk-glade
Requires:	python-pyxdg
Requires:	rb_libtorrent
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
%patch1 -p1

%build
## We forcibly don't store the installation directory during the build, so
## we need to ensure that it is properly inserted into the code as required.
%{__sed} -i -e "s:INSTALL_PREFIX = '@datadir@':INSTALL_PREFIX = '%{_usr}':" \
	src/common.py
%ifarch %{x8664} ppc64 sparc64
	CFLAGS="%{rpmcflags} -DAMD64" %{__python} setup.py build
%else
	CFLAGS="%{rpmcflags}" %{__python} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

## ...then strip the unneeded shebang lines from some of the plugins...
# this seems, wrong, we don't pkg the .py
# and if we do chmod -x on files should not fill autodeps
#sed -i 1d $RPM_BUILD_ROOT%{py_sitedir}/%{name}/{delugegtk.py,delugeplugins.py}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%{py_sitedir}/%{name}-%{version}-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/%{name}
