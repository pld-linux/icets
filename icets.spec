Summary:	Utility for changing IceWM's themes
Summary(pl.UTF-8):	Narzędzie zmieniające motyw graficzny IceWM-a
Name:		icets
Version:	0.8
Release:	6
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
# Source0-md5:	93bde7e212c091759b0259c3c7fc08ad
Source1:	%{name}.desktop
Patch0:		%{name}-themes-path.patch
Patch1:		%{name}-sigsegv.patch
URL:		http://www.selena.kherson.ua/xvadim/programse.html#icets
BuildRequires:	automake
BuildRequires:	qt-devel >= 3.0.5
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small utility allows you to change IceWM's theme without editing
file preferences.

%description -l pl.UTF-8
To małe narzędzie pozwala na zmianę motywu graficznego IceWM-a bez
edycji pliku preferences.

%prep
%setup -q -n %{name}-08
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure2_13 \
	--enable-mt \
	--with-qt-libraries=%{_libdir}
%{__make} \
	icets_LDADD="-lqt-mt -lXext -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install icets/icets $RPM_BUILD_ROOT%{_bindir}
install icets/hi32-app-icets.png $RPM_BUILD_ROOT%{_pixmapsdir}/icets.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README icets/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
