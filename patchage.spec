Summary:	Modular patch bay for audio and MIDI systems
Name:		patchage
Version:	0.5.0
Release:	4
License:	GPL v2
Group:		Applications
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	3f1c297c8c6b998563d1a2fbc215cf85
Patch0:		%{name}-desktop.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	flowcanvas-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libglademm-devel
BuildRequires:	libgnomecanvasmm-devel
BuildRequires:	raul-devel
Provides:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q
%patch0 -p1

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CCFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
./waf configure --nocache --prefix=%{_prefix}
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor/512x512

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/patchage.1*

