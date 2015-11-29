#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	peppercorn
Summary:	A library for converting a token stream into a data structure for use in web form posts
Name:		python-%{module}
Version:	0.4
Release:	2
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/peppercorn/peppercorn-%{version}.tar.gz
# Source0-md5:	464d6f2342eaf704dfb52046c1f5c320
URL:		http://docs.pylonsproject.org/projects/peppercorn/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for converting a token stream into a data structure
comprised of sequences, mappings, and scalars, developed primarily for
converting HTTP form post data into a richer data structure.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests.py*

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
