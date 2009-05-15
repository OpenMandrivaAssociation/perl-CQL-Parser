%define module   CQL-Parser
%define version    1.0
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Represents a base string and modifier strings
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CQL/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Clone)
BuildRequires: perl(String::Tokenizer)
BuildRequires: perl(Test::Exception)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
All the CQL node classes inherit from CQL::Node. CQL::Node essentially
gurantees that its children implements some methods.

toCQL()
toXCQL()
toSwish()
toLucene()
clone()
    Creates a copy of a node, and it's children. Useful if you want to
    modify the tree but keep a copy of the original.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

