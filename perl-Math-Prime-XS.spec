#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Prime-XS
Summary:	Math::Prime::XS - Calculate/detect prime numbers with deterministic tests
#Summary(pl.UTF-8):	
Name:		perl-Math-Prime-XS
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5bd7727093742cc85cd6c762422c98c8
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Math-Prime-XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-boolean
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Prime::XS calculates/detects prime numbers by either applying
Modulo operator division, the Sieve of Eratosthenes, Trial division or
a Summing calculation.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
	#config="optimize='%{rpmcflags}'" \
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorarch}/Math/Prime/XS.pm
%dir %{perl_vendorarch}/auto/Math/Prime/XS
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Prime/XS/*.so
%{_mandir}/man3/*
