Summary:	Program execution path analysis tool
Summary(pl):	Narzêdzie do ¶ledzenia wykonywania programu
Name:		fenris
Version:	0.01b_2332
Release:	1
License:	GPL
Group:		Development/Debuggers
Vendor:		Michal Zalewski <lcamtuf@bos.bindview.com>
Source0:	http://razor.bindview.com/tools/fenris/%{name}.tgz
URL:		http://razor.bindview.com/tools/fenris/
BuildRequires:	binutils-static
BuildRequires:	gdb
BuildRequires:	kernel-source
BuildRequires:	openssl-devel
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
Fenris jest uniwersalnym tracerem, analizatorem i po czê¶ci
dekompilatorem, maj±cym na celu uproszczenie wy³apywania b³êdów,
kontroli bezpieczeñstwa, analizy kodu, algorytmu czy protoko³u -
- dostarczaj±c strukturalnego ¶ledzenia programu, ogólnych informacji
na temat wewnêtrznych konstrukcji, ¶cie¿ek wywo³ania, operacji na
pamiêci, I/O, wyra¿eñ regularnych i wielu innych. Jako ¿e nie wymaga
kodu ¼ród³owego czy jakiej¶ wyró¿nionej metody kompilacji, projekt ten
mo¿e byæ bardzo pomocny przy testach i wykonaniach 'czarnych skrzynek'
- ale bêdzie równie¿ dobrym narzêdziem do kontroli projektów Open
Source, jako niezrównane narzêdzie rekonesanu real-time - szczególnie
je¶li ¼ród³a s± zbyt z³o¿one b±d¼ zbyt ¼le napisane, aby je rzetelnie
analizowaæ w rozs±dnym czasie.

%prep
%setup -q -n %{name}

%build
./build strip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1}

install fnprints.dat $RPM_BUILD_ROOT%{_sysconfdir}
install fenris $RPM_BUILD_ROOT%{_bindir}
install fenris-bug $RPM_BUILD_ROOT%{_bindir}
install fprints $RPM_BUILD_ROOT%{_bindir}
install getfprints $RPM_BUILD_ROOT%{_bindir}
install ragnarok $RPM_BUILD_ROOT%{_bindir}
install ragsplit $RPM_BUILD_ROOT%{_bindir}
install spliter.pl $RPM_BUILD_ROOT%{_bindir}
install doc/man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{ChangeLog,README,TODO,reverse.txt} html/{razor,*html,*.jpg}
%config %verify(not md5 size mtime) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
