Name:           smcroute
Version:        2.2.2
Release:        1%{?dist}
Summary:        Static multicast routing daemon for UNIX 

Group:          System Environment/Daemons
License:        GPL
URL:            http://troglobit.com/smcroute.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://ftp.troglobit.com/smcroute/%{name}-%{version}.tar.xz

# https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(libite) = 1.4.2

BuildRequires:      systemd
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd


%description
SMCRoute is a daemon and command line tool to manipulate the multicast routing table in the UNIX kernel. 

%prep
%setup -q


%build
%configure
export CFLAGS="$RPM_OPT_FLAGS"
autogen.sh
configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install-strip DESTDIR=${RPM_BUILD_ROOT}
rm $RPM_BUILD_ROOT/usr/share/doc/smroute/COPYING


%clean
rm -rf $RPM_BUILD_ROOT


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%defattr(-,root,root,-)
%{_sbindir}/smcroute
%{_mandir}/man8/*
%license COPYING 
%doc README.md AUTHORS CONTRIBUTING.md ChangeLog.md TODO.md
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service


%changelog
* Mon May 15 2017 Matthew Taylor <taylor.matthewd@gmail.com> - 2.2.2-1
  Inital Build
