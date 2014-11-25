#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	Vigenere
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::Vigenere Perl module - Vigenere cipher implementation
Summary(pl.UTF-8):	Moduł Perla Crypt::Vigenere - implementacja szyfru Vigenere
Name:		perl-Crypt-Vigenere
Version:	0.08
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7fb92b19c5022e446ae1a51322e5d061
URL:		http://search.cpan.org/dist/Crypt-Vigenere/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules allows you to recreate the workings of the cryptographic
cipher invented several hundred years ago by a French cryptographer,
Blaise de Vigenere.

%description -l en.UTF-8
This modules allows you to recreate the workings of the cryptographic
cipher invented several hundred years ago by a French cryptographer,
Blaise de Vigenère.

%description -l pl.UTF-8
Ten moduł pozwala na odtworzenie prac związanych z szyfrem wymyślonym
kilkaset lat temu przez francuskiego kryptografa, Blaise de Vigenère.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/Vigenere.pm
%{_mandir}/man3/*
