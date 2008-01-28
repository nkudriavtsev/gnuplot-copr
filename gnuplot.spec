Summary: A program for plotting mathematical expressions and data
Name: gnuplot
Version: 4.0.0
Release: 19%{?dist}
License: distributable
# Modifications are to be distributed as patches to the released version.
Group: Applications/Engineering
Source: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2: gnuplot-init.el
Patch0: gnuplot-4.0.0-x11segv.patch
Patch1: gnuplot-4.0.0-refers_to.patch
BuildRequires: libpng-devel, tetex-latex, zlib-devel, libX11-devel, emacs
BuildRequires: texinfo, readline-devel, libXt-devel, gd-devel, wxGTK-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
Requires: %{name} = %{version}-%{release}, emacs

%description emacs
The gnuplot-emacs package contains the emacs related .el files so that gnuplot
nicely interacts and integrates into emacs.

%prep
%setup -q
%patch0 -p 1 -b .x11segv
%patch1 -p1 -b .refto

%build
%configure --with-readline=gnu --with-png --without-linux-vga \
 --enable-history-file

make %{?_smp_mflags}

rm demo/webify.pl
cd docs
make html
cd psdoc
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_datadir}/emacs/site-lisp/site-start.d/
install -m 644 %SOURCE2 ${RPM_BUILD_ROOT}%{_datadir}/emacs/site-lisp/site-start.d/gnuplot-init.el
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%post 
/sbin/install-info --quiet %{_infodir}/gnuplot.info.gz %{_infodir}/dir || :

%preun
if [ "$1" = "0" ] ; then # last uninstall
   /sbin/install-info --delete %{_infodir}/gnuplot.info.gz %{_infodir}/dir || :
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc BUGS ChangeLog Copyright FAQ NEWS README TODO docs/gnuplot.html 
%doc docs/psdoc/ps_guide.ps docs/psdoc/ps_symbols.gpi tutorial/tutorial.dvi demo
%dir %{_libexecdir}/gnuplot
%dir %{_libexecdir}/gnuplot/4.0
%{_libexecdir}/gnuplot/4.0/gnuplot_x11
%{_bindir}/gnuplot
%{_mandir}/man1/gnuplot.1.gz
%dir %{_datadir}/gnuplot
%dir %{_datadir}/gnuplot/4.0
%{_datadir}/gnuplot/4.0/gnuplot.gih
%{_infodir}/gnuplot.info.gz

%files emacs
%defattr(-,root,root,-)
%{_datadir}/emacs/site-lisp/gnuplot-gui.el
%{_datadir}/emacs/site-lisp/gnuplot-gui.elc
%{_datadir}/emacs/site-lisp/gnuplot.el
%{_datadir}/emacs/site-lisp/gnuplot.elc
%{_datadir}/emacs/site-lisp/info-look.20.2.el
%{_datadir}/emacs/site-lisp/info-look.20.3.el
%{_datadir}/emacs/site-lisp/site-start.d/gnuplot-init.el


%changelog
* Mon Jan 28 2008 Ivana Varekova <varekova@redhat.com> - 4.0.0-19
- add wxGTK-devel dependency (#405411)

* Mon Mar 26 2007 Ivana Varekova <varekova@redhat.com> - 4.0.0-18
- add missing directories (#233838)

* Thu Mar 15 2007 Ivana Varekova <varekova@redhat.com> - 4.0.0-17
- incorporate the package review feedback

* Mon Jan 22 2007 Ivana Varekova <varekova@redhat.com> - 4.0.0-16
- Resolves: 223693  
  fix non-failsafe install-info problem

* Fri Dec 22 2006 Ivana Varekova <varekova@redhat.com> - 4.0.0-15
- Resolves: 173752
  gnuplot refers to /usr/X11R6/lib/fonts/Type1

* Tue Dec 21 2006 Ivana Varekova <varekova@redhat.com> - 4.0.0-14
- remove --without-gd options (#173922, #172565)
- spec file cleanup

* Fri Dec  1 2006 Ivana Varekova <varekova@redhat.com> - 4.0.0-13
- rebuild against libncurses

* Wed Jul 26 2006 Jesse Keating <jkeating@redhat.com> - 4.0.0-12
- rebuild

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 4.0.0-11
- BuildRequires: libXt-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.0.0-10.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.0.0-10.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 02 2005 Phil Knirsch <pknirsch@redhat.com> 4.0.0-10
- Switched BuildPreReqs and Requires to modular xorg-x11 style

* Fri Oct 21 2005 Phil Knirsch <pknirsch@redhat.com> 4.0.0-9
- Fixed 64bit problem with x11 display (#167508)
- Added missing file ownage of /usr/share/gnuplot (#169333)

* Fri Sep 02 2005 Phil Knirsch <pknirsch@redhat.com> 4.0.0-8
- Fixed missing Requires: emacs for the gnuplot-emacs package
- Added a gnuplot-init.el file for startup (#151122)

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 4.0.0-7
- bump release and rebuild with gcc 4

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 4.0.0-6
- Rebuilt for new readline.

* Thu Dec 23 2004 Phil Knirsch <pknirsch@redhat.com> 4.0.0-5
- Added BUGS ChangeLog Copyright FAQ NEWS README TODO to docs (#139070)

* Mon Oct 11 2004 Tim Waugh <twaugh@redhat.com> 4.0.0-4
- Build requires texinfo and readline-devel (bug #134922)

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
