#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Vigenere
Summary:	Crypt::Vigenere Perl module - Vigenere cipher implementation
Summary(pl):	Modu³ Perla Crypt::Vigenere - implementacja szyfru Vigenere
Name:		perl-Crypt-Vigenere
Version:	0.07
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules allows you to recreate the workings of the cryptographic
cipher invented several hundred years ago by a French cryptographer,
Blaise de Vigenère.

%description -l pl
Ten modu³ pozwala na odtworzenie prac zwi±zanych z szyfrem wymy¶lonym
kilkaset lat temu przez francuskiego kryptografa, Blaise de Vigenere.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/Vigenere.pm
%{_mandir}/man3/*
