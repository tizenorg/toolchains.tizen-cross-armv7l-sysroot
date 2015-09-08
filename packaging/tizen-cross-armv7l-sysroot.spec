# spec file for cross-chroot accelerator
#
# Copyright (c) 2010  Jan-Simon Möller (jsmoeller@linuxfoundation.org)
#
Name:           tizen-cross-armv7l-sysroot
ExclusiveArch:  %ix86
AutoReqProv:    0
AutoReqProv:    off
Version:        0.0.1
Release:        1
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        This provides the sysroot file structure
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:  -rpmlint-Factory -rpmlint-mini -post-build-checks tar

%description
Needed for cross-build on x86 side to host the arm cross sysroot

%prep

%build

%install
#rpm -ql filesystem is too much.
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/etc
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/dev
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/proc
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/sys
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/bin
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/lib
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/sbin
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/usr/bin
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/usr/lib
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/usr/sbin
mkdir -p %buildroot/opt/cross/armv7l-tizen-linux-gnueabi/sys-root/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/cross
