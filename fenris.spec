Summary:	Program execution path analysis tool
Summary(pl.UTF-8):   Narzędzie do śledzenia wykonywania programu
Name:		fenris
Version:	0.07
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	http://razor.bindview.com/tools/fenris/%{name}.tgz
# Source0-md5:	14c1fe47e00fd5fc1f7e72f12c056334
Patch0:		%{name}-build_with_sh.patch
Patch1:		%{name}-ncurses.patch
URL:		http://razor.bindview.com/tools/fenris/
BuildRequires:	awk
BuildRequires:	binutils-static
BuildRequires:	fileutils
BuildRequires:	gdb
BuildRequires:	grep
BuildRequires:	kernel-source
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	readline-devel
BuildRequires:	screen
BuildRequires:	sh-utils
BuildRequires:	tar
BuildRequires:	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fenris is a multipurpose tracer, stateful analyzer and partial
decompiler intended to simplify bug tracking, security audits, code,
algorithm or protocol analysis - providing a structural program trace,
general information about internal constructions, execution path,
memory operations, I/O, conditional expressions and much more. Because
it does not require sources or any particular compilation method, this
project can be very helpful for black-box tests and evaluations - but
it will also be a great tool for open-source project audits, as an
unmatched real-time reconnaissance tool - especially when sources are
too complex or too badly written to be analyzed in a reliable way and
reasonable time.

%description -l pl.UTF-8
Fenris jest uniwersalnym tracerem, analizatorem i po części
dekompilatorem, mającym na celu uproszczenie wyłapywania błędów,
kontroli bezpieczeństwa, analizy kodu, algorytmu czy protokołu -
- dostarczając strukturalnego śledzenia programu, ogólnych informacji
na temat wewnętrznych konstrukcji, ścieżek wywołania, operacji na
pamięci, I/O, wyrażeń regularnych i wielu innych. Jako że nie wymaga
kodu źródłowego czy jakiejś wyróżnionej metody kompilacji, projekt ten
może być bardzo pomocny przy testach i wykonaniach 'czarnych skrzynek'
- ale będzie również dobrym narzędziem do kontroli projektów Open
Source, jako niezrównane narzędzie rekonesansu real-time - szczególnie
jeśli źródła są zbyt złożone bądź zbyt źle napisane, aby je rzetelnie
analizować w rozsądnym czasie.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
./build strip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}

install fnprints.dat $RPM_BUILD_ROOT%{_sysconfdir}
install aegir $RPM_BUILD_ROOT%{_bindir}
install dress $RPM_BUILD_ROOT%{_bindir}
install fenris $RPM_BUILD_ROOT%{_bindir}
install fenris-bug $RPM_BUILD_ROOT%{_bindir}
install fprints $RPM_BUILD_ROOT%{_bindir}
install getfprints $RPM_BUILD_ROOT%{_bindir}
install nc-aegir $RPM_BUILD_ROOT%{_bindir}
install ragnarok $RPM_BUILD_ROOT%{_bindir}
install ragsplit $RPM_BUILD_ROOT%{_bindir}
install spliter.pl $RPM_BUILD_ROOT%{_bindir}
install doc/man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{ChangeLog,README,TODO,{anti-fenris,be,debug-api,other,reverse}.txt} html/{razor,samples,*html,*.jpg}
%config %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
