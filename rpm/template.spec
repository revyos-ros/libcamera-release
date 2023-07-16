%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-libcamera
Version:        0.1.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS libcamera package

License:        LGPL-2.1
URL:            https://libcamera.org
Source0:        %{name}-%{version}.tar.gz

Requires:       libatomic
Requires:       libudev-devel
Requires:       libyaml-devel
Requires:       openssl-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  libatomic
BuildRequires:  libudev-devel
BuildRequires:  libyaml-devel
BuildRequires:  meson
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python3-jinja2
BuildRequires:  python3-ply
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
An open source camera stack and framework for Linux, Android, and ChromeOS

%prep
%autosetup -p1

%build
# override macro
%define __meson_auto_features auto
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
# call meson executable instead of using the 'meson' macro to use default paths
%__meson setup \
    --prefix="/opt/ros/humble" \
    --cmake-prefix-path="/opt/ros/humble" \
    --libdir=lib \
    --libexecdir=lib \
    %{_target_platform}
%meson_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%meson_install -C %{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__ninja -C %{_target_platform} -t targets | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%meson_test -C %{_target_platform} || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Sun Jul 16 2023 Christian Rauch <Rauch.Christian@gmx.de> - 0.1.0-1
- Autogenerated by Bloom

* Mon May 01 2023 Christian Rauch <Rauch.Christian@gmx.de> - 0.0.5-1
- Autogenerated by Bloom

* Sun Apr 23 2023 Christian Rauch <Rauch.Christian@gmx.de> - 0.0.4-7
- Autogenerated by Bloom

* Mon Apr 10 2023 Christian Rauch <Rauch.Christian@gmx.de> - 0.0.4-6
- Autogenerated by Bloom

* Tue Apr 04 2023 Christian Rauch <Rauch.Christian@gmx.de> - 0.0.4-5
- Autogenerated by Bloom

* Sun Apr 02 2023 Christian Rauch <Rauch.Christian@gmx.de> - 0.0.4-4
- Autogenerated by Bloom

