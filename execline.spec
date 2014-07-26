Name:		execline
Version:	1.3.1.1
Release:	1%{?dist}
Summary:	execline is a (non-interactive) scripting language, like sh ; but its syntax is quite different from a traditional shell syntax. The execlineb program is meant to be used as an interpreter for a text file; the other commands are essentially useful inside an execlineb script.

Group:		System Environment/Libraries
License:	ISC
URL:		http://skarnet.org/software/execline/index.html
Source0:	http://skarnet.org/software/execline/%{name}-%{version}.tar.gz

BuildRequires:  glibc
BuildRequires:	skalibs
Requires:	skalibs

%description
execline is a (non-interactive) scripting language, like sh ; but its syntax is quite different from a traditional shell syntax. The execlineb program is meant to be used as an interpreter for a text file; the other commands are essentially useful inside an execlineb script.

%prep
%setup -qn prog/%{name}-%{version}
# We want to use FHS so remove flag-slashpackage
%{__rm} -f %{_builddir}/prog/%{name}-%{version}/conf-compile/flag-slashpackage

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
/bin/background
/bin/backtick
/bin/cd
/bin/define
/bin/dollarat
/bin/elgetopt
/bin/elgetpositionals
/bin/elglob
/bin/emptyenv
/bin/exec
/bin/execlineb
/bin/exit
/bin/export
/bin/fdblock
/bin/fdclose
/bin/fdmove
/bin/fdreserve
/bin/forbacktickx
/bin/foreground
/bin/forx
/bin/getpid
/bin/heredoc
/bin/homeof
/bin/if
/bin/ifelse
/bin/ifte
/bin/ifthenelse
/bin/import
/bin/importas
/bin/loopwhilex
/bin/multidefine
/bin/multisubstitute
/bin/pipeline
/bin/piperw
/bin/redirfd
/bin/runblock
/bin/shift
/bin/tryexec
/bin/umask
/bin/unexport
/bin/wait
/lib/libexecline.so
/lib/libexecline.so.1
/lib/libexecline.so.1.3
/lib/libexecline.so.1.3.1.1
/lib/libexecline.so.api.3.1
/usr/include/execline/execline-config.h
/usr/include/execline/execline.h
/usr/lib/execline/libexecline.a

%changelog
* Sat Jul 26 2014 Ian Meyer <ianmmeyer@gmail.com> - 1.3.1.1-1
- Initial RPM release of execline

