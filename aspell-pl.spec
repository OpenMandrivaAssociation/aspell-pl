%define src_ver 6.0
%define snap 20090208
%define relsnap %{snap}-0
%define languageeng polish
%define languageenglazy Polish
%define languagecode pl
%define lc_ctype pl_PL

%define fname aspell6-pl-%{snap}

Summary:	%{languageenglazy} dictionary for aspell
Name:		aspell-pl
Version:	0.60.5
Release:	%mkrel 2.%{snap}.4
License:	GPLv2+
Group:		System/Internationalization
URL:		http://www.kurnik.pl/slownik/ort/
Source0:	http://www.kurnik.org/dictionary/sjp-aspell6-%{languagecode}-%{src_ver}_%{relsnap}.tar.bz2
BuildRequires:	aspell >= 0.60.5
Requires:	aspell >= %{version}
Provides:	spell-%{languagecode}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buidroot

%description
Polish dictionary (i.e. word list) for aspell.

%prep
%setup -qn aspell6-%{languagecode}-%{src_ver}_%{relsnap}

%build
# note: configure is not autoconf-generated
./configure

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README doc/*
%{_libdir}/aspell-*/*
