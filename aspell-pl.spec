%define src_ver %(echo %{version} |cut -d_ -f1)
%define snap %(echo %{version} |cut -d_ -f2)
%define relsnap %{snap}-0
%define languageeng polish
%define languageenglazy Polish
%define languagecode pl
%define lc_ctype pl_PL

%define fname aspell6-pl-%{snap}

Summary:	%{languageenglazy} dictionary for aspell
Name:		aspell-pl
Version:	6.0_20230701
Release:	1
License:	GPLv2+
Group:		System/Internationalization
Url:		http://www.sjp.pl/slownik/ort/
Source0:	http://sjp.pl/slownik/ort/sjp-aspell6-%{languagecode}-%{src_ver}_%{relsnap}.tar.bz2
BuildArch:	noarch

BuildRequires:	aspell >= 0.60.5
Requires:	aspell >= 0.%{src_ver}
Provides:	spell-%{languagecode}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}

%description
Polish dictionary (i.e. word list) for aspell.

%prep
%setup -qn aspell6-%{languagecode}-%{src_ver}_%{relsnap}

%build
# note:	configure is not autoconf-generated
./configure

%make

%install
%makeinstall_std

%files
%doc README doc/*
%{_libdir}/aspell-*/*

