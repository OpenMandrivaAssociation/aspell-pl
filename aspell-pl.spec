%define src_ver 6.0
%define snap 20061121-0
%define languageeng polish
%define languageenglazy Polish
%define languagecode pl
%define lc_ctype pl_PL

%define fname aspell6-pl-%{snap}

Summary:	%{languageenglazy} dictionary for aspell
Name:		aspell-pl
Version:	0.60.5
Release:	%mkrel 1
License:	Creative Commons ShareAlike
Group:		System/Internationalization
URL:		http://aspell.sourceforge.net/
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}_%{snap}.tar.bz2
BuildRequires:	aspell >= 0.60.5
Requires:	aspell >= %{version}
Provides:	spell-%{languagecode}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buidroot

# Mandrake Stuff
Requires:	locales-%{languagecode}
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}

%description
Polish dictionary (i.e. word list) for aspell.

%prep
%setup -qn aspell6-%{languagecode}-%{src_ver}_%{snap}

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
%doc README Copyright doc/*
%{_libdir}/aspell-*/*


