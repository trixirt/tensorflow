%global commit0 35a58b7b886f7991a2f82a01d9bd27153a47fc0f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        A library to detect information about host CPU
Name:           tensorflow-lite
License:        BSD
Version:        2.9.3
%define patch_level 1
Release:        %{patch_level}.git%{?shortcommit0}%{?dist}

URL:            https://github.com/tensorflow/tensorflow
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# gcc 13 cstdint
Patch0:         0001-include-cstdint.patch

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
%autosetup -p1 -n tensorflow-%{commit0}

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


