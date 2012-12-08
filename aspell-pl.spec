%define src_ver 6.0
%define snap 20110628
%define relsnap %{snap}-0
%define languageeng polish
%define languageenglazy Polish
%define languagecode pl
%define lc_ctype pl_PL

%define fname aspell6-pl-%{snap}

Summary:	%{languageenglazy} dictionary for aspell
Name:		aspell-pl
Version:	0.60.5
Release:	3.%{snap}.2
License:	GPLv2+
Group:		System/Internationalization
URL:		http://www.sjp.pl/slownik/ort/
Source0:	http://sjp.pl/slownik/ort/sjp-aspell6-%{languagecode}-%{src_ver}_%{relsnap}.tar.bz2
BuildRequires:	aspell >= 0.60.5
Requires:	aspell >= %{version}
Provides:	spell-%{languagecode}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
BuildArch:	noarch

%description
Polish dictionary (i.e. word list) for aspell.

%prep
%setup -qn aspell6-%{languagecode}-%{src_ver}_%{relsnap}

%build
# note: configure is not autoconf-generated
./configure

%make

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README doc/*
%{_libdir}/aspell-*/*


%changelog
* Tue Jun 28 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-3.20110628.1mdv2011.0
+ Revision: 687945
- update to new snapshot 20110628
- update urls for website and source

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.5-2.20090830.9
+ Revision: 662861
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.5-2.20090830.8mdv2011.0
+ Revision: 603453
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.5-2.20090830.7mdv2010.1
+ Revision: 518954
- rebuild

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20090830.6mdv2010.0
+ Revision: 422488
- new snapshot 20090830

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.60.5-2.20090208.5mdv2010.0
+ Revision: 413096
- rebuild

* Sun Feb 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20090208.4mdv2009.1
+ Revision: 338606
- new snapshot 20090208

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20080825.3mdv2009.0
+ Revision: 275727
- new snapshot

* Sat Jun 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20080628.3mdv2009.0
+ Revision: 229806
- update to new snapshot 20080628

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.60.5-2.20080303.2mdv2008.1
+ Revision: 182603
- provide enchant-dictionary

* Mon Mar 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20080303.1mdv2008.1
+ Revision: 178050
- new snapshot

* Mon Jan 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20080128.1mdv2008.1
+ Revision: 159230
- new snapshot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20071128.1mdv2008.1
+ Revision: 113734
- new snapshot
- new license policy
- do not package Copyright file

  + Thierry Vignaud <tv@mandriva.org>
    - s/Mandrake/Mandriva/

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-2.20070825.1mdv2008.0
+ Revision: 71254
- switch to an alternative dictionary (better maintained)
- spec file clean


* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.60.5-1mdv2007.0
+ Revision: 119947
- Import aspell-pl

* Tue Oct 11 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.51.0-3mdk
- update (using affix compression, thus resulting in smaller package)

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.51.0-2mdk
- rebuild for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.51.0-1mdk
- updated to 0.51.0

