Name:           smcroute
Version:        2.1.1
Release:        1%{?dist}
Summary:        Static multicast routing daemon for UNIX 

Group:          System Environment/Daemons
License:        GPL
URL:            http://troglobit.com/smcroute.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://ftp.troglobit.com/smcroute/%{name}-%{version}.tar.xz

# https://fedorahosted.org/fpc/tickeet/174
Provides:       bundled(libite) = 1.4.2

%if 0%{?el6}
BuildRequires:  libcap-devel
%else
BuildRequires:  systemd, libcap-devel
%endif


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

install -d -m 755 %{buildroot}%{_sysconfdir}/init.d
install -p -m 755 %{buildroot}/usr/share/doc/%{name}/smcroute.init %{buildroot}/etc/init.d/smcroute


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sbindir}/smcroute
%{_mandir}/man8/*
%license COPYING
/usr/share/doc/smcroute/*
/etc/init.d/smcroute

%changelog
* Mon May 15 2017 Matthew Taylor <taylor.matthewd@gmail.com> - 2.2.2-1
  Inital Build
