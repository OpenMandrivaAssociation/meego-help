Name: meego-help
Summary: MeeGo Help
Version: 0.0.2
Release: 1.8
Group: System/Desktop
License: LGPL 2.1
URL: http://www.meego.com
Source0: %{name}-%{version}.tar.gz
Requires: desktop-file-utils
BuildRequires: libglib2-devel
BuildRequires: libdbus-glib-1-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: desktop-file-utils

%description
MeeGo help documentation

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/*

%post
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/meego-help/*
%{_datadir}/applications/meego-help.desktop
%{_bindir}/meego-help

