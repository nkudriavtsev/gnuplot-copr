Summary: A program for plotting mathematical expressions and data.
Name: gnuplot
Version: 3.7.1
Release: 12
License: distributable
Group: Applications/Engineering
Source: ftp://ftp.gnuplot.vt.edu/pub/gnuplot/gnuplot-%{version}.tar.gz
Patch0: gnuplot-3.7.1-gd-1.8.patch
BuildPrereq: gd-devel >= 1.8.2, libpng-devel, tetex-latex, zlib-devel
Requires: gd >= 1.8.2, libpng
BuildRoot: %{_tmppath}/%{name}-root
URL: http://www.gnuplot.vt.edu/

%description
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

Install gnuplot if you need a graphics package for scientific data
representation.

%prep
%setup -q
%patch -p1 -b .gd-1.8

%build
%ifarch alpha
%define optflags -O0
%endif
%configure --with-readline=gnu --with-png --without-linux-vga

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

cd docs
make doc2html
./doc2html gnuplot.doc > gnuplot.html
cd latextut
PATH=$RPM_BUILD_DIR/gnuplot-%{version}:$PATH make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/gnuplot}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -m 755 -s gnuplot_x11 $RPM_BUILD_ROOT/usr/bin/gnuplot_x11
install -m 755 -s gnuplot $RPM_BUILD_ROOT/usr/bin/gnuplot
install -m 644 docs/gnuplot.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 docs/gnuplot.gih $RPM_BUILD_ROOT/usr/share/gnuplot.gih

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/gnuplot.html docs/psdoc docs/latextut/tutorial.dvi demo
/usr/bin/gnuplot_x11
/usr/bin/gnuplot
%{_mandir}/man1/gnuplot.*
/usr/share/gnuplot.gih

%changelog
* Tue Aug 22 2000 Bill Nottingham <notting@redhat.com>
- remove zlib-devel requirement (#16718)

* Wed Aug 02 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild with libpng 1.0.8

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 18 2000 Bill Nottingham <notting@redhat.com>
- fix  manpage paths

* Fri Jun  9 2000 Bill Nottingham <notting@redhat.com>
- rebuild in new environment

* Fri May 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild with new gd, changing gif terminal to jpeg terminal (release 7)

* Mon May 08 2000 Preston Brown <pbrown@redhat.com>
- build for 7.0

* Thu Apr  6 2000 Bill Nottingham <notting@redhat.com>
- use gnu readline, not built-in version

* Mon Apr  3 2000 Bill Nottingham <notting@redhat.com>
- add latex tutorial, demo files, other docs (#10508)

* Wed Mar  1 2000 Bill Nottingham <notting@redhat.com>
- update to 3.7.1. Oops.

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Thu Nov  4 1999 Bill Nottingham <notting@redhat.com>
- update to 3.7.1

* Mon Oct 11 1999 Bill Nottingham <notting@redhat.com>
- ship some docs.

* Wed Aug 18 1999 Bill Nottingham <notting@redhat.com>
- add a patch to fix postscript output from Bernd Kischnick
 (kisch@die-herrmanns.de)

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- fix license

* Thu Jul 15 1999 Bill Nottingham <notting@redhat.com>
- rebuild without svgalib

* Tue Jun 15 1999 Bill Nottingham <notting@redhat.com>
- update to 3.7.0.1

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.7.

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.6beta347

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
