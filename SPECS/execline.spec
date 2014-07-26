Name:		execline
Version:	1.3.1.1
Release:	1%{?dist}
Summary:	execline is a (non-interactive) scripting language, like sh ; but its syntax is quite different from a traditional shell syntax. The execlineb program is meant to be used as an interpreter for a text file; the other commands are essentially useful inside an execlineb script.

Group:		System Environment/Libraries
License:	ISC
URL:		http://skarnet.org/software/%{name}/index.html
Source0:	http://skarnet.org/software/%{name}/%{name}-%{version}.tar.gz
patch0:		update-package-export-to-support-DESTDIR.diff
patch1:		update-paths-for-FHS.diff
BuildRequires:  glibc
BuildRequires:	skalibs

%description
execline is a (non-interactive) scripting language, like sh ; but its syntax is quite different from a traditional shell syntax. The execlineb program is meant to be used as an interpreter for a text file; the other commands are essentially useful inside an execlineb script.

%prep
%setup -qn admin/%{name}-%{version}
# We want to use FHS so remove flag-slashpackage
%{__rm} -f %{_builddir}/admin/%{name}-%{version}/conf-compile/flag-slashpackage
%patch0 -p1
%patch1 -p1

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

