Summary: A program for plotting mathematical expressions and data.
Name: gnuplot
Version: 4.0.0
Release: 4
License: Redistributable, with restrictions
Group: Applications/Engineering
Source: http://prdownloads.sourceforge.net/gnuplot/gnuplot-4.0.0.tar.gz
BuildPrereq: libpng-devel, tetex-latex, zlib-devel, xorg-x11-devel, emacs
BuildRequires: texinfo, readline-devel
Requires: libpng
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.gnuplot.info/

%description
Gnuplot is a command-line driven, interactive function plotting
program especially suited for scientific data representation.  Gnuplot
can be used to plot functions and data points in both two and three
dimensions and in many different formats.

Install gnuplot if you need a graphics package for scientific data
representation.

%package emacs
Group: Applications/Engineering
Summary: Emacs bindings for the gnuplot main application
Requires: %{name} = %{version}-%{release}

%description emacs
The gnuplot-emacs package contains the emacs related .el files so that gnuplot
nicely interacts and integrates into emacs.

%prep
%setup -q

%build
%configure --with-readline=gnu --with-png --without-linux-vga \
 --without-gd --enable-history-file

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

cd docs
make html
PATH=$RPM_BUILD_DIR/gnuplot-%{version}:$PATH make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%post 
if [ "$1" = "1" ] ; then  # first install
 if [ -x /sbin/install-info ]; then
   /sbin/install-info %{_infodir}/gnuplot.info.gz %{_infodir}/dir
 fi
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
 if [ -x /sbin/install-info ]; then
   /sbin/install-info --delete %{_infodir}/gnuplot.info.gz %{_infodir}/dir
 fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/gnuplot.html docs/psdoc tutorial/tutorial.dvi demo
%{_libexecdir}/gnuplot/4.0/gnuplot_x11
%{_bindir}/gnuplot
%{_mandir}/man1/gnuplot.1.gz
%{_datadir}/gnuplot/4.0/gnuplot.gih
%{_infodir}/gnuplot.info.gz

%files emacs
%defattr(-,root,root)
%{_datadir}/emacs/site-lisp/gnuplot-gui.el
%{_datadir}/emacs/site-lisp/gnuplot-gui.elc
%{_datadir}/emacs/site-lisp/gnuplot.el
%{_datadir}/emacs/site-lisp/gnuplot.elc
%{_datadir}/emacs/site-lisp/info-look.20.2.el
%{_datadir}/emacs/site-lisp/info-look.20.3.el


%changelog
* Mon Oct 11 2004 Tim Waugh <twaugh@redhat.com> 4.0.0-4
- Build requires texinfo and readline-devel (bug #134922).

* Tue Sep 07 2004 Karsten Hopp <karsten@redhat.de> 4.0.0-3 
- fix typo in preun script

* Thu Sep  2 2004 Bill Nottingham <notting@redhat.com> 4.0.0-2
- %%defattr fixes (#131640)

* Thu Aug 12 2004 Phil Knirsch <pknirsch@redhat.com> 4.0.0-1
- Update to gnuplot-4.0.0
- Split off emacs files into new subpackage

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jul 02 2003 Bill Nottingham <notting@redhat.com> 3.7.3-4
- fix license (#98449)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Bill Nottingham <notting@redhat.com> 3.7.3-1
- update to 3.7.3
- don't bother patching it to do jpegs with gd instead of gifs,
  as we haven't been building it with gd support anyway

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 3.7.2-2
- remove unpackaged files from the buildroot

* Thu Jul 18 2002 Bill Nottingham <notting@redhat.com> 3.7.2-1
- update to 3.7.2

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 23 2002 Bill Nottingham <notting@redhat.com> 3.7.1-16
- fix bug #43620 (<broeker@physik.rwth-aachen.de>)

* Tue Jan 22 2002 Bill Nottingham <notting@redhat.com> 3.7.1-15
- fix bug #21341 (<wtcorrea@cs.princeton.edu>)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 11 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.7.1-13
- rebuild with new readline
- Fix up License: and URL: tags in specfile

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
