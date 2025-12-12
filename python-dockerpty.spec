%global upstream_name dockerpty

Name:           python-%{upstream_name}
Version:        0.4.1
Release:        12%{?dist}1
Summary:        Python library to use the pseudo-tty of a docker container
License:        ASL 2.0
URL:            https://github.com/d11wtq/dockerpty
Source0:        %{url}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz
BuildRequires:  python-setuptools
BuildRequires:  python-devel
BuildRequires:  python-six
BuildArch:      noarch

%global _description\
Provides the functionality needed to operate the pseudo-tty (PTY) allocated to\
a docker container, using the Python client

%description    %{_description}

%package -n python2-%{upstream_name}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-six
%{?python_provide:%python_provide python2-%{upstream_name}}

%description -n python2-%{upstream_name} %{_description}

%prep
%autosetup -n %{upstream_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

# we are missing the 'expects' library to run the tests
# %%check
# LANG=en_US.utf8 py.test-%%{python3_version} -vv tests
# LANG=en_US.utf8 py.test-%%{python2_version} -vv tests

%files -n python2-%{upstream_name}
%license LICENSE.txt
%doc README.md MANIFEST.in
%{python2_sitelib}/%{upstream_name}
%{python2_sitelib}/%{upstream_name}-%{version}-py%{python2_version}.egg-info

%files
%license LICENSE.txt
%doc README.md MANIFEST.in
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-%{version}-py%{python3_version}.egg-info
