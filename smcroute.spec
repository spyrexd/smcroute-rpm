Name:           smcroute
Version:        2.2.2
Release:        1%{?dist}
Summary:        Static multicast routing daemon for UNIX 

Group:          System Environment/Daemons
License:        GPL
URL:            http://troglobit.com/smcroute.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://ftp.troglobit.com/smcroute/%{name}-%{version}.tar.xz

# https://fedorahosted.org/fpc/tickeet/174
Provides:       bundled(libite) = 1.4.2

BuildRequires:  libcap-devel


%description
SMCRoute is a daemon and command line tool to manipulate the multicast routing table in the UNIX kernel. 

%prep
%setup -q


%build
%configure
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}
make install-man DESTDIR=${RPM_BUILD_ROOT}

%if 0%{?el6}
mkdir -p %{buildroot}%{_sysconfdir}/init.d
ln -s /usr/share/doc/smcroute/smcroute.init %{_sysconfdir}/init.d/smcroute
rm %{buildroot}%{_unitdir}
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sbindir}/smcroute
%{_mandir}/man8/*
%license COPYING
%doc README.md AUTHORS ChangeLog.md TODO COPYING smcroute.conf
%doc smcroute.conf smcroute.init 
%if 0%{?el6}
%{_sysconfdir}/init.d/smcroute
%else
%{_unitdir}/%{name}.service
%endif

%changelog
* Mon May 15 2017 Matthew Taylor <taylor.matthewd@gmail.com> - 2.2.2-1
  Inital Build
