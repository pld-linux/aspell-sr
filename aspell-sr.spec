Summary:	Serbian dictionary for aspell
Summary(pl.UTF-8):	Słownik serbski dla aspella
Name:		aspell-sr
Version:	0.02
Release:	3
License:	LGPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/sr/aspell6-sr-%{version}.tar.bz2
# Source0-md5:	a068ba095e7246fd3bbc92e7d0287998
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serbian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik serbski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-sr-%{version}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{Changelog,README}
%lang(sr) %doc doc/{PROCITAJME*,Promene*,Uputstvo*}
%{_prefix}/lib/aspell/*
%{_datadir}/aspell/*
