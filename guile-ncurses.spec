Summary:	Guile-Ncurses - Guile library with functions for creating text user interface
Summary(pl.UTF-8):	Guile-Ncurses - biblioteka Guile z funkcjami do tworzenia tekstowego interfejsu użytkownika
Name:		guile-ncurses
Version:	3.1
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/guile-ncurses/%{name}-%{version}.tar.gz
# Source0-md5:	ade6a07fdafcea7f177eb0642d96da6a
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/guile-ncurses/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
# 2.2 and 3.0 supported
BuildRequires:	guile-devel >= 5:2.2
BuildRequires:	libtool >= 2:2
BuildRequires:	libunistring-devel
BuildRequires:	ncurses-devel >= 5
BuildRequires:	ncurses-ext-devel >= 5
BuildRequires:	pkgconfig
BuildRequires:	texinfo
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	guile >= 5:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Guile-Ncurses is a library for the Guile Scheme interpreter that
provides functions for creating text user interfaces. The text user
interface functionality is built on the ncurses libraries: curses,
form, panel, and menu.

%description -l pl.UTF-8
GNU Guile-Ncurses to biblioteka interpretera Scheme Guile
udostępniająca funkcje do tworzenia tekstowego interfejsu użytkownika.
Funkcjonalność ta jest zbudowana w oparciu o biblioteki ncurses:
curses, form, panel i menu.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/3.*/extensions/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/guile-ncurses-shell
%attr(755,root,root) %{_libdir}/guile/3.*/extensions/libguile-ncurses.so*
%{_libdir}/guile/3.*/site-ccache/ncurses
%{_datadir}/guile/site/3.*/ncurses
%{_infodir}/guile-ncurses.info*
