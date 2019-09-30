Name: osinfo-db-tools
Version: 1.2.0
Release: 3
Summary: Tools to manage the osinfo database
License: GPLv2+
URL: http://libosinfo.org/
Source: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.gz

BuildRequires: gcc glib2-devel intltool libarchive-devel perl-podlators
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0

%description
Osinfo-db-tools contains set of tools to assist administrators and
developers in managing the osinfo database.

%package help
Summary: Help files for %{name}
BuildArch: noarch
%description help
Help files for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build V=1

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%doc AUTHORS ChangeLog NEWS README
%license COPYING

%files help
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
* Mon Aug 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.0-3
- Package init
