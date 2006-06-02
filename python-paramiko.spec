%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define srcname paramiko

Name:           python-paramiko
Version:        1.6
Release:        1%{?dist}
Summary:        A SSH2 protocol library for python

Group:          Development/Libraries
License:        LGPL
URL:            http://www.lag.net/paramiko/
Source0:        http://www.lag.net/paramiko/download/%{srcname}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-abi = %{pyver}
Requires:       python-crypto >= 1.9

%description
Paramiko (a combination of the esperanto words for "paranoid" and "friend") is
a module for python 2.3 or greater that implements the SSH2 protocol for secure
(encrypted and authenticated) connections to remote machines. Unlike SSL (aka
TLS), the SSH2 protocol does not require heirarchical certificates signed by a
powerful central authority. You may know SSH2 as the protocol that replaced
telnet and rsh for secure access to remote shells, but the protocol also
includes the ability to open arbitrary channels to remote services across an
encrypted tunnel. (This is how sftp works, for example.)

%prep
%setup -q -n %{srcname}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --single-version-externally-managed


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE PKG-INFO README docs/
%{python_sitelib}/paramiko-%{version}-py%{pyver}.egg-info
%dir %{python_sitelib}/paramiko
%{python_sitelib}/paramiko/*.py
%{python_sitelib}/paramiko/*.pyc
%ghost %{python_sitelib}/paramiko/*.pyo

%changelog
* Fri Jun 02 2006 Shahms E. King <shahms@shahms.com> 1.6-1
- Update to new upstream version
- ghost the .pyo files

* Fri May 05 2006 Shahms E. King <shahms@shahms.com> 1.5.4-2
- Fix source line and rebuild

* Fri May 05 2006 Shahms E. King <shahms@shahms.com> 1.5.4-1
- Update to new upstream version

* Wed Apr 12 2006 Shahms E. King <shahms@shahms.com> 1.5.3-1
  - Initial package
