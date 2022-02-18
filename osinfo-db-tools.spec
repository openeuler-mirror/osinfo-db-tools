Name: osinfo-db-tools
Version: 1.8.0
Release: 2
Summary: Tools to manage the osinfo database
License: GPLv2+
URL: http://libosinfo.org/
Source: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz

BuildRequires: meson json-glib-devel libsoup-devel python3 python3-pytest python3-requests 
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
%meson
%meson_build

%check
%ifarch riscv64
# Fix poor performance
%meson_test --timeout-multiplier 10
%else
%meson_test 
%endif

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%doc NEWS README
%license COPYING

%files help
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
* Sat Feb 19 2022 YukariChiba <i@0x7f.cc> - 1.8.0-2
- Fix unit test timeout for RISC-V

* Sat Jan 23 2021 zoulin <zoulin@huawei.com> - 1.8.0-1
- update version to 1.8.0

* Tue Sep 8 2020 linwei <linwei54@openeuler.org> - 1.2.0-4
- Modify the URL of Source

* Mon Aug 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.0-3
- Package init
