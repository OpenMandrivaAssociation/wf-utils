%define major 0
%define libpackage %mklibname wf-utils %{major}
%define devpackage %mklibname -d wf-utils

%define git 20210516

Name:           wf-utils
Version:        0.4.0
Release:        1.%{git}.1
Summary:        Contains utility classes for Wayfire
Group:          Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wf-utils
# There is no release or tags yet. So for now use master branch
Source0:        https://github.com/WayfireWM/wf-utils/archive/refs/heads/%{name}-master.tar.gz
 
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(glm)

%description
Contains utility classes for Wayfire
 
%package -n %{libpackage}
Summary:	Libraries for wf-utils
Group:		System/Libraries/Wayfire 
Provides: wf-utils

%description -n %{libpackage}
Libraries for wf-utils

%package -n %{devpackage}
Summary:	Development files for wf-utils
Group:		System/Libraries
Requires:	%{libpackage} = %{EVRD}

%description -n %{devpackage}
Development files for wf-utils

%prep
%autosetup -n %{name}-master -p1
 

%build
%meson
 
%meson_build
 
%install
%meson_install
 
%files -n %{libpackage}
%{_libdir}/libwf-utils.so.%{major}*

%files -n %{devpackage}
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/wf-utils.pc
%{_includedir}/wayfire/
