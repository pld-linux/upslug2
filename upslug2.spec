# TODO:
#	- check Version and License
#
%define svn_revision 40
%define snapshot_date 20071120

Summary:	Firmware update utility for the NSLU2
Name:		upslug2
Version:	0.12
Release:	0.svn%{svn_revision}.1
License:	MIT
Group:		Development/Tools
# snapshot from http://svn.nslu2-linux.org/svnroot/upslug2/trunk
Source0:	%{name}-%{snapshot_date}.tar.bz2
# Source0-md5:	c14930873d3f3c26fdc5dc57f885958f
URL:		http://www.nslu2-linux.org/wiki/Main/UpSlug2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
upslug2 is a command line program intended to allow the upgrade of a
LinkSys NSLU2 firmware to new or different versions. Unlike upslug and
the LinkSys (Sercomm) upgrade utilities, upslug2 will synthesise a
complete 'image' from a kernel and a root file system, as such it
duplicates part of the functionality of 'slugimage'.

upslug2 also optimizes the upload to avoid transmitted parts of the
image which need not be written or are 'blank' (set to the erased
flash value of all 1's).

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-libpcap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_mandir}/man8
install upslug2.8 $RPM_BUILD_ROOT/%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/upslug2
%{_mandir}/man8/upslug2.8*
