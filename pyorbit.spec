%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

### Abstract ###

Name: pyorbit
Version: 2.24.0
Release: 5%{?dist}
License: LGPLv2+
Group: Development/Languages
Summary: Python bindings for ORBit2.
BuildRoot: %{_tmppath}/%{name}-root
Source0: http://ftp.gnome.org/pub/GNOME/sources/pyorbit/2.24/%{name}-%{version}.tar.bz2

Obsoletes: orbit-python

### Dependencies ###

Requires: ORBit2 >= 2.3.103
Requires: glib2 >= 2.4.0
Requires: libIDL >= 0.8.0
Requires: python2 >= 2.3

### Build Dependencies ###

BuildRequires: ORBit2-devel >= 2.6.0
BuildRequires: autoconf
BuildRequires: automake >= 1.6.3-5
BuildRequires: glib2-devel >= 2.4.0
BuildRequires: libIDL-devel >= 0.8.0
BuildRequires: libtool
BuildRequires: pygtk2 >= 2.4.0
BuildRequires: python2-devel >= 2.3

%description
pyorbit is an extension module for python that gives you access
to the ORBit2 CORBA ORB.

%package devel
Summary: Files needed to build wrappers for ORBit2 addon libraries.
Group: Development/Languages
Obsoletes: orbit-python-devel
Requires: %{name} = %{version}

%description devel
This package contains files required to build wrappers for ORBit2 addon
libraries so that they interoperate with pyorbit

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README ChangeLog

%defattr(755, root, root, 755)
%{python_sitearch}/*.so
%defattr(644, root, root, 755)
%{python_sitearch}/*.py*

%files devel
%defattr(644, root, root, 755)
%{_includedir}/pyorbit-2
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-5
- Fix the major version number in the Source URI.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.24.0-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.24.0-2
- Rebuild for Python 2.6

* Tue Sep 23 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-1.fc10
- Update to 2.24.0

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.14.3-3
- fix license tag

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.3-2.fc8
- Rebuild with GCC 4.3

* Wed Oct 10 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.3-1.fc8
- Update to 2.14.3

* Tue Apr 17 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.2-2.fc7
- Fix some file permissions (RH bug #236738).
- Spec file cleanups.

* Sun Feb 25 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.2-1.fc7
- Update to 2.14.2

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.14.1-2
- rebuild for python 2.5

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.14.1-1.1
- rebuild

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-1
- Update to 2.14.1

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Apr 16 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License:

* Fri Nov 26 2004 Florian La Roche <laroche@redhat.com>
- add %%clean target

* Sun Nov  7 2004 Jeremy Katz <katzj@redhat.com> - 2.0.1-2
- rebuild for python 2.4

* Tue Sep 28 2004 Mark McLoughlin <markmc@redhat.com> 2.0.0-5
- Remove linc requires
- Fix multilib issue

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-2
- rebuild for python 2.3

* Thu Sep  4 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-1
- 2.0.0

* Wed Aug 20 2003 Jeremy Katz <katzj@redhat.com> 1.99.6-1
- 1.99.6

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb  6 2003 Matt Wilson <msw@redhat.com> 1.99.3-5
- rebuild against new python

* Tue Jan 28 2003 Jeremy Katz <katzj@redhat.com> 1.99.3-4
- libdir-ify

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Dec 28 2002 Jeremy Katz <katzj@redhat.com> 1.99.3-2
- fix defattr

* Fri Dec 27 2002 Jeremy Katz <katzj@redhat.com> 1.99.3-1
- update to pyorbit 1.99.3, obsolete orbit-python

* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- use %%configure and %%makeinstall
- don't install .la files
- use %%_libdir for pkgconfig files

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Feb 27 2002 Matt Wilson <msw@redhat.com>
- initial package

