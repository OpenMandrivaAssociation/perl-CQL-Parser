%define upstream_name    CQL-Parser
%define upstream_version 1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    compiles CQL strings into parse trees of Node subtypes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CQL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Clone)
BuildRequires: perl(String::Tokenizer)
BuildRequires: perl(Test::Exception)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/CQL
