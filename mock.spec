Summary: Builds packages inside chroots
Name: mock
Version: 0.1
Release: 1
License: GPL
Group: Development/Tools
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}root
BuildRequires: gcc
Requires: python, yum >= 2.3.2
Requires(pre): shadow-utils


%description
Mock takes a srpm and builds it in a chroot

%prep
%setup -q

%build
make


%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%pre
groupadd -r mock >/dev/null 2>&1

%postun
groupdel mock >/dev/null 2>&1

%files
%defattr(-, root, root)
%doc README 
%dir  %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%{_bindir}/%{name}
%attr(04750, root, mock) %{_sbindir}/mock-helper
%attr(02775, root, mock) %dir /var/lib/mock


%changelog
* Sun May 15 2005 Seth Vidal <skvidal@phy.duke.edu>
- first version/packaging
