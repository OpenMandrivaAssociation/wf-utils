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
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
Development files for %{name}.
 
%prep
%autosetup -n %{name}-master -p1
 

%build
%meson
 
%meson_build
 
%install
%meson_install
 
%files
