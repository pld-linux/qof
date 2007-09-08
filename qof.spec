Summary:	Query Object Framework
Summary(pl.UTF-8):	Obiektowy szkielet zapytań
Name:		qof
Version:	0.7.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/qof/%{name}-%{version}.tar.gz
# Source0-md5:	dff6bfda556544a240e833d22e509b50
Patch0:		%{name}-link.patch
URL:		http://qof.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	libgda-devel >= 1:1.2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.5.10
BuildRequires:	perl-base >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	sqlite-devel >= 2.8.0
Requires:	glib2 >= 1:2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QOF is an offshoot of the GnuCash engine, consisting of those pieces
unrelated to accounting. The Query Engine allows C/C++ applications
to treat random collections of objects as if they were SQL tables,
and perform table-join type queries across them. In addition, the
query engine can be backed by an actual database, so that instances
of local objects can act as a 'cache' to a much larger SQL database.

%description -l pl.UTF-8
QOF to odprysk silnika GnuCasha, składający się z części nie
związanych z finansami. Silnik zapytań pozwala aplikacjom C/C++
traktować dowolne kolekcje obiektów tak, jakby były tabelami SQL i
wykonywać na nich zapytania z łączeniem tabel. Ponadto silnik zapytań
może być powiązany z właściwą bazą danych, dzięki czemu instancje
obiektów lokalnych mogą służyć jako "pamięć podręczna" dla dużo
większej bazy danych SQL.

%package devel
Summary:	Header files for QOF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QOF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.10.0
Requires:	libgda-devel >= 1:1.2.0

%description devel
Header files for QOF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki QOF.

%package static
Summary:	Static QOF libraries
Summary(pl.UTF-8):	Statyczne biblioteki QOF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static QOF libraries.

%description static -l pl.UTF-8
Statyczne biblioteki QOF.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-doxygen \
	--enable-sqlite
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened
rm -f $RPM_BUILD_ROOT%{_libdir}/libqof-backend-*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libqof.so.*.*.*
%attr(755,root,root) %{_libdir}/libqof-backend-qsf.so.*.*.*
%attr(755,root,root) %{_libdir}/libqof-backend-qsf.so
%attr(755,root,root) %{_libdir}/libqof-backend-sqlite.so.*.*.*
%attr(755,root,root) %{_libdir}/libqof-backend-sqlite.so
%{_datadir}/xml/qof

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libqof.so
%{_libdir}/libqof.la
%{_includedir}/qof
%{_pkgconfigdir}/qof-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libqof.a
