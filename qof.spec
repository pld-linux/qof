# TODO: fix shared libs linking, -devel deps
Summary:	Query Object Framework
Summary(pl):	Obiektowy szkielet zapytañ
Name:		qof
Version:	0.6.1
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/qof/%{name}-%{version}.tar.gz
# Source0-md5:	2a1c4b231fb03e49d5d9237dc6698c3e
URL:		http://qof.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgda-devel >= 1.2.0
BuildRequires:	libxml2-devel >= 1:2.5.10
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QOF is an offshoot of the GnuCash engine, consisting of those pieces
unrelated to accounting. The Query Engine allows C/C++ applications
to treat random collections of objects as if they were SQL tables,
and perform table-join type queries across them. In addition, the
query engine can be backed by an actual database, so that instances
of local objects can act as a 'cache' to a much larger SQL database.

%description -l pl
QOF to odprysk silnika GnuCasha, sk³adaj±cy siê z czê¶ci nie
zwi±zanych z finansami. Silnik zapytañ pozwala aplikacjom C/C++
traktowaæ dowolne kolekcje obiektów tak, jakby by³y tabelami SQL i
wykonywaæ na nich zapytania z ³±czeniem tabel. Ponadto silnik zapytañ
mo¿e byæ powi±zany z w³a¶ciw± baz± danych, dziêki czemu instancje
obiektów lokalnych mog± s³u¿yæ jako "pamiêæ podrêczna" dla du¿o
wiêkszej bazy danych SQL.

%package devel
Summary:	Header files for QOF library
Summary(pl):	Pliki nag³ówkowe biblioteki QOF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for QOF library.

%description devel -l pl
Pliki nag³ówkowe biblioteki QOF.

%package static
Summary:	Static QOF libraries
Summary(pl):	Statyczne biblioteki QOF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static QOF libraries.

%description static -l pl
Statyczne biblioteki QOF.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libqof*.so.*.*.*
%{_datadir}/xml/qof

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libqof*.so
%{_libdir}/libqof*.la
%{_includedir}/qof
%{_pkgconfigdir}/qof-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libqof*.a
