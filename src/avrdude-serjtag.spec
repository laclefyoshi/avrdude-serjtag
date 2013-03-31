## -*- mode: rpm-spec; -*-
##
## $Id: avrdude.spec.in 558 2005-11-29 20:28:51Z joerg_wunsch $
##
## avrdude.spec.  Generated from avrdude.spec.in by configure.
##

%define debug_package %{nil}

%define _with_docs 0
%{?_without_docs: %define _with_docs 0}
%define _with_ftd2xx 1
%{?_without_ftd2xx: %define _with_ftd2xx 0}

Summary: AVRDUDE is software for programming Atmel AVR Microcontrollers.
Name: avrdude
Version: 5.10
Release: serjtag0.4k
URL: http://ftp.twaren.net/Unix/NonGNU/avrdude/
#URL: http://mirror.cinquix.com/pub/savannah/avrdude

Source0: %{name}-%{version}.tar.gz
NoSource:0
Patch1: avrdude-5.8-confwin.patch
Patch2: avrdude-5.8-usbasp.patch
Patch3: avrdude-5.8-baud.patch
Patch4: avrdude-5.10-serjtag.patch
Patch5: avrdude-5.8-ft245r.patch
Patch6: avrdude-5.8-conf.patch
Patch7: avrdude-5.8-confu2.patch
Patch8: avrdude-5.10-usbasp2.patch
Patch9: avrdude-5.10-confd3.patch
Patch10: avrdude-5.10-ser_posix-fix.patch
License: GPL
Group: Development/Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%if %{_with_docs}
## The avrdude-docs subpackage
%package docs
Summary: Documentation for AVRDUDE.
Group: Documentation
%description docs
Documentation for avrdude in info, html, postscript and pdf formats.
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build

./configure \
%if %{_with_ftd2xx}
	CFLAGS="-g -O2 -DSUPPORT_FT245R" LIBS="-lftd2xx" \
%endif
	--prefix=%{_prefix} --sysconfdir=/etc --mandir=%{_mandir} \
	--infodir=%{_infodir} \
%if %{_with_docs}
	--enable-doc=yes
%else
	--enable-doc=no
%endif


make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/etc \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	install

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%if %{_with_docs}
%post docs
[ -f %{_infodir}/avrdude.info ] && \
	/sbin/install-info %{_infodir}/avrdude.info %{_infodir}/dir || :
[ -f %{_infodir}/avrdude.info.gz ] && \
	/sbin/install-info %{_infodir}/avrdude.info.gz %{_infodir}/dir || :

%preun docs
if [ $1 = 0 ]; then
	[ -f %{_infodir}/avrdude.info ] && \
		/sbin/install-info --delete %{_infodir}/avrdude.info %{_infodir}/dir || :
	[ -f %{_infodir}/avrdude.info.gz ] && \
		/sbin/install-info --delete %{_infodir}/avrdude.info.gz %{_infodir}/dir || :
fi
%endif

%files
%defattr(-,root,root)
%{_prefix}/bin/avrdude
%{_mandir}/man1/avrdude.1.gz
%attr(0644,root,root)   %config /etc/avrdude.conf

%if %{_with_docs}
%files docs
%doc %{_infodir}/*info*
%doc doc/avrdude-html/*.html
%doc doc/TODO
%doc doc/avrdude.ps
%doc doc/avrdude.pdf
%endif

%changelog
* Fri Sep 23 2005 Galen Seitz <galens@seitzassoc.com>
- Default to enable-doc=yes during configure.
- Move info file to docs package.
- Make building of docs package conditional.  Basic idea copied from avr-gcc.

* Wed Aug 27 2003 Theodore A. Roth <troth@openavr.org>
  [Thanks to Artur Lipowski <LAL@pro.onet.pl>]
- Do not build debug package.
- Remove files not packaged to quell RH9 rpmbuild complaints.

* Wed Mar 05 2003 Theodore A. Roth <troth@openavr.org>
- Add docs sub-package.
- Add %post and %preun scriptlets for handling info files.

* Wed Feb 26 2003 Theodore A. Roth <troth@openavr.org>
- Initial build.


