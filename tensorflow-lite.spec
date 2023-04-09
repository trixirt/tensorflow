Summary:        A library to detect information about host CPU
Name:           tensorflow-lite
License:        BSD
Version:        2.12.0
%define patch_level 1
Release:        %{patch_level}%{?dist}

URL:            https://github.com/tensorflow/tensorflow
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

# use fedora flatbuffers
Patch0:         0001-cmake-flatbuffers.patch
# gcc 13 cstdint
Patch1:         0001-include-cstdint.patch


Group:          Development/Libraries
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
TBD

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the developement libraries and headers
for %{name}.

%prep
%autosetup -p1 -n tensorflow-%{version}

%build
%cmake tensorflow/lite \
       -DCMAKE_INSTALL_PREFIX=/usr \
       -DBUILD_SHARED_LIBS=ON \
       -DTFLITE_ENABLE_GPU=ON \
       -DTFLITE_ENABLE_RUY=OFF \
       -DTFLITE_ENABLE_XNNPACK=OFF \
       -DTFLITE_ENABLE_NNAPI=OFF \
       -DTFLITE_ENABLE_RESOURCE=OFF

%cmake_build

%install
%cmake_install

%files

%files devel

%changelog
* Sun Apr 9 2023 Tom Rix <trix@redhat.com> - 2.12.0-1

