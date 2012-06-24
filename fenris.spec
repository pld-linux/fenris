Summary:	Program execution path analysis tool
Summary(pl):	Narz�dzie do �ledzenia wykonywania programu
Name:		fenris
Version:	0.01b_3091
Release:	1
License:	GPL
Group:		Development/Debuggers
Vendor:		Michal Zalewski <lcamtuf@bos.bindview.com>
Source0:	http://razor.bindview.com/tools/fenris/%{name}.tgz
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
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	sed
BuildRequires:	screen
BuildRequires:	sh-utils
BuildRequires:	textutils
BuildRequires:	tar
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

%description -l pl
Fenris jest uniwersalnym tracerem, analizatorem i po cz�ci
dekompilatorem, maj�cym na celu uproszczenie wy�apywania b��d�w,
kontroli bezpiecze�stwa, analizy kodu, algorytmu czy protoko�u -
- dostarczaj�c strukturalnego �ledzenia programu, og�lnych informacji
na temat wewn�trznych konstrukcji, �cie�ek wywo�ania, operacji na
pami�ci, I/O, wyra�e� regularnych i wielu innych. Jako �e nie wymaga
kodu �r�d�owego czy jakiej� wyr�nionej metody kompilacji, projekt ten
mo�e by� bardzo pomocny przy testach i wykonaniach 'czarnych skrzynek'
- ale b�dzie r�wnie� dobrym narz�dziem do kontroli projekt�w Open
Source, jako niezr�wnane narz�dzie rekonesanu real-time - szczeg�lnie
je�li �r�d�a s� zbyt z�o�one b�d� zbyt �le napisane, aby je rzetelnie
analizowa� w rozs�dnym czasie.

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
%config %verify(not md5 size mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
