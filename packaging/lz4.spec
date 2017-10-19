#
# spec file for package lz4
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           lz4
%define lname	liblz4-1
Version:        1.8.0
Release:        0
Summary:        Hash-based Predictive LempelZiv compressor
License:        GPL-2.0+ and BSD-2-Clause
Group:          Productivity/Archiving/Compression
Url:            http://lz4.org/

#Git-Clone:	https://github.com/lz4/lz4
Source0:        %{name}-%{version}.tar.gz
Source1001:	lz4.manifest
Patch1:         lz4-use-shlib.diff
Patch2:         lz-export.diff
BuildRequires:  pkg-config
BuildRequires:	perl

%description
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(LempelZiv) family of byte-oriented compression schemes. It is a
LZP2 fork and provides better compression ratio for text files.

This subpackage provides a GPL command-line utility to make use of
the LZ4 algorithm.

%package -n %lname
Summary:        Hash-based predictive Lempel-Ziv compressor
License:        BSD-2-Clause
Group:          System/Libraries

%description -n %lname
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(LempelZiv) family of byte-oriented compression schemes. It is a

This subpackage contains the (de)compressor code as a shared library.

%package -n liblz4-devel
Summary:        Development files for the LZ4 compressor
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n liblz4-devel
LZ4 is a lossless data compression algorithm that is focused on
compression and decompression speed. It belongs to the LZ77
(LempelZiv) family of byte-oriented compression schemes. It is a

This subpackage contains libraries and header files for developing
applications that want to make use of liblz4.

%prep
%setup -q
cp %{SOURCE1001} .
%patch -P 1 -P 2 -p1

%build
# Goddammit, lz4
perl -i -pe 's{^\t@}{\t}g' Makefile */Makefile
# don't bother building here, because make install builds it again - unconditionally :-(

%install
make install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}"
rm -Rf %{buildroot}%{_mandir}

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%manifest lz4.manifest
%defattr(-,root,root)
%_bindir/lz4*
%_bindir/unlz4

%files -n %lname
%defattr(-,root,root)
%_libdir/liblz4.so.1*

%files -n liblz4-devel
%defattr(-,root,root)
%_includedir/lz4*.h
%_libdir/liblz4.so
%_libdir/pkgconfig/*.pc
%_libdir/*.a

%changelog

