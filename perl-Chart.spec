%define	module	Chart
%define	name	perl-%{module}
%define	version	2.4.1
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A series of charting modules
License:	GPL
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/C/CH/CHARTGRP/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl-GD
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Series of charting modules.

%prep
%setup -q -n %{module}-%{version}
chmod 0644 README TODO

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README TODO
%{perl_vendorlib}/Chart*
%{_mandir}/*/*

