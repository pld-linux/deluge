Summary:	A Python BitTorrent client with support for UPnP and DHT
Summary(pl.UTF-8):	Klient BitTorrenta napisany w pythonie ze wspraciem dla UPnP i DHT
Name:		deluge
Version:	0.4.99.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
URL:		http://deluge-torrent.org/
Source0:	http://deluge-torrent.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	e4f9b3a39dfecf793dfcd62f2ccb1286
#Source1:	%{name}-fixed-setup.py
BuildRequires:	boost-program_options-devel
BuildRequires:	boost-regex-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	rb_libtorrent-devel
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

%prep
%setup -q
#install -m 0755 %{SOURCE1} ./setup.py


%build
## We forcibly don't store the installation directory during the build, so
## we need to ensure that it is properly inserted into the code as required.
%{__sed} -i -e "s:INSTALL_PREFIX = '@datadir@':INSTALL_PREFIX = '%{_usr}':" \
	src/dcommon.py
%ifarch x86_64 ppc64 sparc64
	CFLAGS="%{optflags} -DAMD64" %{__python} setup.py build
%else
	CFLAGS="%{optflags}" %{__python} setup.py build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

## ...then strip the unneeded shebang lines from some of the plugins...
for FILE in $RPM_BUILD_ROOT%{py_sitedir}/%{name}/{delugegtk.py,delugeplugins.py}; do
	sed -i 1d ${FILE};
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitedir}/%{name}/
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}/*.so
%{py_sitedir}/%{name}-%{version}-py2.5.egg-info
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_pixmapsdir}/%{name}.xpm
