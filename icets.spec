Summary:	Utility for changing IceWM's themes
Summary(pl):	Narz�dzie zmieniaj�ce temat graficzny IceWM'a
Name:		icets
Version:	0.8
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.selena.kherson.ua/xvadim/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-themes-path.patch
URL:		http://www.selena.kherson.ua/xvadim/programse.html#icets
BuildRequires:	qt-devel
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This small utility allows you to change IceWM's theme without editing
file preferences.

%description -l pl
To ma�e narz�dzie pozwala na zmian� tematu graficznego IceWM'a bez
edytowania pliku preferences.

%prep
%setup -q -n %{name}-08
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

install icets/icets $RPM_BUILD_ROOT%{_bindir}
install icets/hi32-app-icets.png $RPM_BUILD_ROOT%{_pixmapsdir}/icets.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM/

gzip -9nf AUTHORS ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz icets/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Settings/IceWM/*
