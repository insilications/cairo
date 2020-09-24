#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cairo
Version  : 1.16.0
Release  : 70
URL      : https://www.cairographics.org/releases/cairo-1.16.0.tar.xz
Source0  : https://www.cairographics.org/releases/cairo-1.16.0.tar.xz
Summary  : Multi-platform 2D graphics library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1
Requires: cairo-bin = %{version}-%{release}
Requires: cairo-lib = %{version}-%{release}
Requires: cairo-license = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : grep
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : librsvg-dev
BuildRequires : libxcb-dev
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : systemd-dev
Patch1: madvise.patch
Patch2: CVE-2019-6461.patch
Patch3: CVE-2019-6462.patch
Patch4: CVE-2018-19876.patch

%description
Cairo - Multi-platform 2D graphics library
https://cairographics.org
What is cairo
=============
Cairo is a 2D graphics library with support for multiple output
devices. Currently supported output targets include the X Window
System (via both Xlib and XCB), quartz, win32, and image buffers,
as well as PDF, PostScript, and SVG file output. Experimental backends
include OpenGL, BeOS, OS/2, and DirectFB.

%package bin
Summary: bin components for the cairo package.
Group: Binaries
Requires: cairo-license = %{version}-%{release}

%description bin
bin components for the cairo package.


%package dev
Summary: dev components for the cairo package.
Group: Development
Requires: cairo-lib = %{version}-%{release}
Requires: cairo-bin = %{version}-%{release}
Provides: cairo-devel = %{version}-%{release}
Requires: cairo = %{version}-%{release}

%description dev
dev components for the cairo package.


%package doc
Summary: doc components for the cairo package.
Group: Documentation

%description doc
doc components for the cairo package.


%package lib
Summary: lib components for the cairo package.
Group: Libraries
Requires: cairo-license = %{version}-%{release}

%description lib
lib components for the cairo package.


%package license
Summary: license components for the cairo package.
Group: Default

%description license
license components for the cairo package.


%prep
%setup -q -n cairo-1.16.0
cd %{_builddir}/cairo-1.16.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600296481
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --disable-gtk-doc --enable-xlib=yes --enable-xcb=yes --enable-ft=yes --enable-fc=yes --enable-gl --enable-xlib-xcb
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1600296481
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cairo
cp %{_builddir}/cairo-1.16.0/COPYING-LGPL-2.1 %{buildroot}/usr/share/package-licenses/cairo/8088b44375ef05202c0fca4e9e82d47591563609
cp %{_builddir}/cairo-1.16.0/COPYING-MPL-1.1 %{buildroot}/usr/share/package-licenses/cairo/aba8d76d0af67d57da3c3c321caa59f3d242386b
cp %{_builddir}/cairo-1.16.0/perf/COPYING %{buildroot}/usr/share/package-licenses/cairo/2cc384b53d50baa25a960aa83b0ac0edca682fa7
cp %{_builddir}/cairo-1.16.0/test/COPYING %{buildroot}/usr/share/package-licenses/cairo/a4233e56493311ffd59845410b6e156f03b07335
cp %{_builddir}/cairo-1.16.0/test/pdiff/gpl.txt %{buildroot}/usr/share/package-licenses/cairo/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1
cp %{_builddir}/cairo-1.16.0/util/cairo-script/COPYING %{buildroot}/usr/share/package-licenses/cairo/d888f729a340181e37b0b2fb25c2942d5005e6a2
cp %{_builddir}/cairo-1.16.0/util/cairo-trace/COPYING %{buildroot}/usr/share/package-licenses/cairo/0315f8fa18770a489890f8448111722aca24b8ec
cp %{_builddir}/cairo-1.16.0/util/cairo-trace/COPYING-GPL-3 %{buildroot}/usr/share/package-licenses/cairo/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cairo-trace

%files dev
%defattr(-,root,root,-)
/usr/include/cairo/cairo-deprecated.h
/usr/include/cairo/cairo-features.h
/usr/include/cairo/cairo-ft.h
/usr/include/cairo/cairo-gl.h
/usr/include/cairo/cairo-gobject.h
/usr/include/cairo/cairo-pdf.h
/usr/include/cairo/cairo-ps.h
/usr/include/cairo/cairo-script-interpreter.h
/usr/include/cairo/cairo-script.h
/usr/include/cairo/cairo-svg.h
/usr/include/cairo/cairo-version.h
/usr/include/cairo/cairo-xcb.h
/usr/include/cairo/cairo-xlib-xrender.h
/usr/include/cairo/cairo-xlib.h
/usr/include/cairo/cairo.h
/usr/lib64/libcairo-gobject.so
/usr/lib64/libcairo-script-interpreter.so
/usr/lib64/libcairo.so
/usr/lib64/pkgconfig/cairo-egl.pc
/usr/lib64/pkgconfig/cairo-fc.pc
/usr/lib64/pkgconfig/cairo-ft.pc
/usr/lib64/pkgconfig/cairo-gl.pc
/usr/lib64/pkgconfig/cairo-glx.pc
/usr/lib64/pkgconfig/cairo-gobject.pc
/usr/lib64/pkgconfig/cairo-pdf.pc
/usr/lib64/pkgconfig/cairo-png.pc
/usr/lib64/pkgconfig/cairo-ps.pc
/usr/lib64/pkgconfig/cairo-script.pc
/usr/lib64/pkgconfig/cairo-svg.pc
/usr/lib64/pkgconfig/cairo-xcb-shm.pc
/usr/lib64/pkgconfig/cairo-xcb.pc
/usr/lib64/pkgconfig/cairo-xlib-xcb.pc
/usr/lib64/pkgconfig/cairo-xlib-xrender.pc
/usr/lib64/pkgconfig/cairo-xlib.pc
/usr/lib64/pkgconfig/cairo.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/cairo/bindings-errors.html
/usr/share/gtk-doc/html/cairo/bindings-fonts.html
/usr/share/gtk-doc/html/cairo/bindings-memory.html
/usr/share/gtk-doc/html/cairo/bindings-overloading.html
/usr/share/gtk-doc/html/cairo/bindings-path.html
/usr/share/gtk-doc/html/cairo/bindings-patterns.html
/usr/share/gtk-doc/html/cairo/bindings-return-values.html
/usr/share/gtk-doc/html/cairo/bindings-streams.html
/usr/share/gtk-doc/html/cairo/bindings-surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Error-handling.html
/usr/share/gtk-doc/html/cairo/cairo-FreeType-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Image-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-PDF-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-PNG-Support.html
/usr/share/gtk-doc/html/cairo/cairo-Paths.html
/usr/share/gtk-doc/html/cairo/cairo-PostScript-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Quartz-(CGFont)-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Quartz-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Raster-Sources.html
/usr/share/gtk-doc/html/cairo/cairo-Recording-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Regions.html
/usr/share/gtk-doc/html/cairo/cairo-SVG-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Script-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-Tags-and-Links.html
/usr/share/gtk-doc/html/cairo/cairo-Transformations.html
/usr/share/gtk-doc/html/cairo/cairo-Types.html
/usr/share/gtk-doc/html/cairo/cairo-User-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Version-Information.html
/usr/share/gtk-doc/html/cairo/cairo-Win32-Fonts.html
/usr/share/gtk-doc/html/cairo/cairo-Win32-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XCB-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XLib-Surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-XLib-XRender-Backend.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-device-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-font-face-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-font-options-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-matrix-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-pattern-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-scaled-font-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-surface-t.html
/usr/share/gtk-doc/html/cairo/cairo-cairo-t.html
/usr/share/gtk-doc/html/cairo/cairo-drawing.html
/usr/share/gtk-doc/html/cairo/cairo-fonts.html
/usr/share/gtk-doc/html/cairo/cairo-support.html
/usr/share/gtk-doc/html/cairo/cairo-surfaces.html
/usr/share/gtk-doc/html/cairo/cairo-text.html
/usr/share/gtk-doc/html/cairo/cairo.devhelp2
/usr/share/gtk-doc/html/cairo/home.png
/usr/share/gtk-doc/html/cairo/index-1.10.html
/usr/share/gtk-doc/html/cairo/index-1.12.html
/usr/share/gtk-doc/html/cairo/index-1.14.html
/usr/share/gtk-doc/html/cairo/index-1.16.html
/usr/share/gtk-doc/html/cairo/index-1.2.html
/usr/share/gtk-doc/html/cairo/index-1.4.html
/usr/share/gtk-doc/html/cairo/index-1.6.html
/usr/share/gtk-doc/html/cairo/index-1.8.html
/usr/share/gtk-doc/html/cairo/index-all.html
/usr/share/gtk-doc/html/cairo/index.html
/usr/share/gtk-doc/html/cairo/language-bindings.html
/usr/share/gtk-doc/html/cairo/left-insensitive.png
/usr/share/gtk-doc/html/cairo/left.png
/usr/share/gtk-doc/html/cairo/right-insensitive.png
/usr/share/gtk-doc/html/cairo/right.png
/usr/share/gtk-doc/html/cairo/style.css
/usr/share/gtk-doc/html/cairo/up-insensitive.png
/usr/share/gtk-doc/html/cairo/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/cairo/libcairo-trace.so
/usr/lib64/libcairo-gobject.so.2
/usr/lib64/libcairo-gobject.so.2.11600.0
/usr/lib64/libcairo-script-interpreter.so.2
/usr/lib64/libcairo-script-interpreter.so.2.11600.0
/usr/lib64/libcairo.so.2
/usr/lib64/libcairo.so.2.11600.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cairo/0315f8fa18770a489890f8448111722aca24b8ec
/usr/share/package-licenses/cairo/2cc384b53d50baa25a960aa83b0ac0edca682fa7
/usr/share/package-licenses/cairo/8088b44375ef05202c0fca4e9e82d47591563609
/usr/share/package-licenses/cairo/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/cairo/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1
/usr/share/package-licenses/cairo/a4233e56493311ffd59845410b6e156f03b07335
/usr/share/package-licenses/cairo/aba8d76d0af67d57da3c3c321caa59f3d242386b
/usr/share/package-licenses/cairo/d888f729a340181e37b0b2fb25c2942d5005e6a2
