%define upstream_name    CQL-Parser
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Compiles CQL strings into parse trees of Node subtypes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CQL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Clone)
BuildRequires:	perl(String::Tokenizer)
BuildRequires:	perl(Test::Exception)

BuildArch:	noarch

%description
CQL::Parser provides a mechanism to parse Common Query Language (CQL)
statements. The best description of CQL comes from the CQL homepage at
the Library of Congress <http://www.loc.gov/z3950/agency/zing/cql/>

CQL is a formal language for representing queries to information
retrieval systems such as web indexes, bibliographic catalogs and museum
collection information. The CQL design objective is that queries be
human readable and human writable, and that the language be intuitive
while maintaining the expressiveness of more complex languages.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/CQL


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 680704
- mass rebuild

* Fri Dec 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 473269
- update to 1.10

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0-2mdv2010.0
+ Revision: 375957
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2009.1
+ Revision: 355046
- import perl-CQL-Parser


* Sat Mar 14 2009 cpan2dist 1.0-1mdv
- initial mdv release, generated with cpan2dist

