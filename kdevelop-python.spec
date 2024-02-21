%undefine __cmake_in_source_build

Name:           kdevelop-python
Summary:        Python language and documentation plugins for KDevelop
Version:        23.08.5
Release:        1%{?dist}

# Most files LGPLv2+/GPLv2+
License:        GPL-2.0-or-later
URL:            http://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/kdev-python-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  kdevelop-pg-qt-devel >= 1.90.91
BuildRequires:  kdevelop-devel >= %{version}

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  grantlee-qt5-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  python-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel

%{?kdevelop_requires}

%description
%{summary}.


%prep
%setup -q -n kdev-python-%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install

# TODO Enable translations in stable build
%find_lang %{name} --all-name
%files -f %{name}.lang

%{_datadir}/kdevappwizard/
%{_datadir}/kdevpythonsupport/
%{_libdir}/libkdevpython*.so
%{_kf5_qtplugindir}/kdevplatform/
%{_datadir}/qlogging-categories5/kdevpythonsupport.categories
%{_datadir}/metainfo/org.kde.kdev-python.metainfo.xml


%changelog
* Tue Feb 21 2024 Weldon Goree <weldon@librem.one> - 23.08.5
- Upgrade to 23.08.5
* Thu Oct 12 2023 Weldon Goree <weldon@librem.one> - 23.08.1
- Upgrade to 23.08.1
* Tue Aug 08 2023 Weldon Goree <weldon@librem.one> - 23.04.3-1
- Created package
