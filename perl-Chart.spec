%define	upstream_name	 Chart
%define upstream_version 2.4.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.4.6
Release:	2

Summary:	A series of charting modules
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/C/CH/CHARTGRP/Chart-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(GD)

BuildArch:	noarch

%description
Series of charting modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 0644 README TODO

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README TODO
%{perl_vendorlib}/Chart*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.4.2-2mdv2011.0
+ Revision: 680773
- mass rebuild

* Sun Oct 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.4.2-1mdv2011.0
+ Revision: 588697
- update to 2.4.2

* Sat Feb 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.4.1-6mdv2011.0
+ Revision: 505422
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.4.1-5mdv2010.0
+ Revision: 430322
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.4.1-4mdv2009.0
+ Revision: 256401
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.4.1-2mdv2008.1
+ Revision: 136680
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1-2mdv2008.0
+ Revision: 86066
- rebuild


* Fri Feb 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1-1mdk
- New release 2.4.1

* Thu Oct 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.3-3mdk
- Fix BuildRequires
- fix url/source

* Thu Oct 20 2005 Olivier Thauvin <nanardon@mandriva.org> 2.3-2mdk
- rebuild
- add make test

* Mon May 31 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.3-1mdk
- 2.3

* Mon Aug 18 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.2-4mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- rm -rf /home/guillomovitch/rpm/tmp/perl-Chart-2.4.1 in %%install
- use %%makeinstall_std macro
- cosmetics

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.2-2mdk
- rebuild for new auto{prov,req}

* Fri Apr 25 2003 François Pons <fpons@mandrakesoft.com> 2.2-1mdk
- 2.2.

* Fri Apr 25 2003 Pixel <pixel@mandrakesoft.com> 1.0.1-4mdk
- add "BuildRequires: perl-devel"


