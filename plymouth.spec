%define plymouthdaemon_execdir /sbin
%define plymouthclient_execdir /bin
%define plymouth_libdir /%{_lib}

%define _libexecdir %{_prefix}/libexec

%define major 2
%define libname %mklibname %{name} %{major}
%define libply %mklibname ply %{major}
%define libply_boot_client %mklibname ply-boot-client %{major}
%define libply_splash_graphics %mklibname ply-splash-graphics %{major}
%define libply_splash_core %mklibname ply-splash-core %{major}
%define devname %mklibname %{name} -d

%define snapshot 0

%bcond_with uclibc

Summary:	Graphical Boot Animation and Logger
Name:		plymouth
Version:	0.8.8
Release:	13
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.freedesktop.org/wiki/Software/Plymouth
Source0:	http://www.freedesktop.org/software/plymouth/releases/%{name}-%{version}.tar.bz2
Source1:	boot-duration
Source2:	charge.plymouth
# PATCH-OPENSUSE -- Restore suspend / resume state (needed for suspend package)
Patch0:		plymouth-restore-suspend.patch
# PATCH-OPENSUSE -- Handle correctly multiple displays with different sizes
Patch4:		plymouth-fix-window-size
# PATCH-OPENSUSE -- Add line numbers to tracing output
Patch8:		plymouth-0.8.6.1.mkinitrd-to-dracut.patch
# (tpg) sync with current git
Patch10:	0001-tag-0.8.8-5277809e5a95e9fec8a80f2072673b383bcc80cc.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(systemd)
%if %{with uclibc}
BuildRequires:	uClibc-devel
BuildRequires:	libpng-static-devel
%endif
BuildRequires:	systemd-units
%rename		splashy
Requires(post):	plymouth-scripts = %{version}-%{release}
Requires:	initscripts >= 8.83
Requires(post):	dracut
Requires:	desktop-common-data >= 2010.0-1mdv
Conflicts:	systemd-units < 186

%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.

%package system-theme
Group:		System/Kernel and hardware
Summary:	Plymouth default theme
Requires:	plymouth(system-theme)
Requires:	plymouth = %{version}-%{release}

%description system-theme
This metapackage tracks the current distribution default theme.

%package -n %{libply}
Summary:	Plymouth libraries
Group:		System/Libraries
Obsoletes:	%{_lib}plymouth2 < 0.8.8-12

%description -n %{libply}
This package contains the libply library used by Plymouth.

%package -n %{libply_boot_client}
Summary:	Plymouth libraries
Group:		System/Libraries
Conflicts:	%{_lib}plymouth2 < 0.8.8-12

%description -n %{libply_boot_client}
This package contains the libply-boot-client library used by Plymouth.

%package -n %{libply_splash_graphics}
Summary:	Plymouth libraries
Group:		System/Libraries
Conflicts:	%{_lib}plymouth2 < 0.8.8-12

%description -n %{libply_splash_graphics}
This package contains the libply-splash-graphic library used by Plymouth.

%package -n %{libply_splash_core}
Summary:	Plymouth libraries
Group:		System/Libraries
Conflicts:	%{_lib}plymouth2 < 0.8.8-12

%description -n %{libply_splash_core}
This package contains the libply-splash-core library used by Plymouth.

%package -n uclibc-%{libname}
Summary:	Plymouth libraries
Group:		System/Libraries
Conflicts:	%{_lib}plymouth2 < 0.8.8-12

%description -n uclibc-%{libname}
This package contains the libply and libplybootsplash libraries
used by Plymouth.

%package -n %{devname}
Group:		System/Kernel and hardware
Summary:	Libraries and headers for writing Plymouth splash plugins
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libply} = %{version}-%{release}
Requires:	%{libply_boot_client} = %{version}-%{release}
Requires:	%{libply_splash_graphics} = %{version}-%{release}
Requires:	%{libply_splash_core} = %{version}-%{release}
Requires:	uclibc-%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the libply and libplybootsplash libraries
and headers needed to develop 3rd party splash plugins for Plymouth.

%package utils
Group:		System/Kernel and hardware
Summary:	Plymouth related utilities
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains utilities that integrate with Plymouth
including a boot log viewing application.

%package scripts
Group:		System/Kernel and hardware
Summary:	Plymouth related scripts
Conflicts:	mkinitrd < 6.0.92-6mdv
Requires(pre):	%{name} = %{version}-%{release}

%description scripts
This package contains scripts that help integrate Plymouth with
the system.

%package plugin-label
Group:		System/Kernel and hardware
Summary:	Plymouth label plugin

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.

%package plugin-fade-throbber
Group:		System/Kernel and hardware
Summary:	Plymouth "Fade-Throbber" plugin

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

%package plugin-script
Group:		System/Kernel and hardware
Summary:	Plymouth "Script" plugin
Requires:	plymouth-plugin-label = %{version}-%{release}

%description plugin-script
This package contains the "Script" plugin for Plymouth. 

%package theme-script
Group:		System/Kernel and hardware
Summary:	Plymouth "Script" theme
Requires:	%{name}-plugin-script = %{version}-%{release}
Requires(post):	plymouth-scripts = %{version}-%{release}

%description theme-script
This package contains the "Script" boot splash theme for
Plymouth.

%package theme-fade-in
Group:		System/Kernel and hardware
Summary:	Plymouth "Fade-In" theme
Requires:	%{name}-plugin-fade-throbber = %{version}-%{release}
Requires(post):	plymouth-scripts = %{version}-%{release}

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.

%package plugin-throbgress
Group:		System/Kernel and hardware
Summary:	Plymouth "Throbgress" plugin
Requires:	plymouth-plugin-label = %{version}-%{release}

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that
spins repeatedly while a progress bar advances at the bottom of
the screen.

%package theme-spinfinity
Group:		System/Kernel and hardware
Summary:	Plymouth "Spinfinity" theme
Requires:	%{name}-plugin-throbgress = %{version}-%{release}
Requires(post):	plymouth-scripts = %{version}-%{release}

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.

%package theme-spinner
Group:		System/Kernel and hardware
Summary:	Plymouth "Spinner" theme
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Requires(post):	plymouth-scripts = %{version}-%{release}

%description theme-spinner
This package contains the "Spinner" boot splash theme for
Plymouth.

%package plugin-two-step
Group:		System/Kernel and hardware
Summary:	Plymouth "two-step" plugin
Requires:	plymouth-plugin-label = %{version}-%{release}

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

%package plugin-space-flares
Group:		System/Kernel and hardware
Summary:	Plymouth "space-flares" plugin
Requires:	plymouth-plugin-label = %{version}-%{release}

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package theme-solar
Group:		System/Kernel and hardware
Summary:	Plymouth "Solar" theme
Requires:	%{name}-plugin-space-flares = %{version}-%{release}
Requires(post):	plymouth-scripts = %{version}-%{release}

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.

%package theme-charge
Group:		System/Kernel and hardware
Summary:	Plymouth "Charge" plugin
Requires:	%{name}-plugin-two-step = %{version}-%{release}
Requires(post):	plymouth-scripts = %{version}-%{release}

%description theme-charge
This package contains the "charge" boot splash theme for
Plymouth. It features the shadowy hull of a logo charge up and
and finally burst into full form.

%package theme-glow
Group:		System/Kernel and hardware
Summary:	Plymouth "Glow" plugin
Requires(post):	plymouth-scripts  = %{version}-%{release}
Requires:	plymouth-plugin-two-step = %{version}-%{release}

%description theme-glow
This package contains the "Glow" boot splash theme for Plymouth.

%package plugin-tribar
Group:		System/Kernel and hardware
Summary:	Plymouth "tribar" plugin
Requires:	plymouth-plugin-label = %{version}-%{release}

%description plugin-tribar
This package contains the "tribar" boot splash plugin for
Plymouth.

%package theme-tribar
Group:		System/Kernel and hardware
Summary:	Plymouth "Tribar" plugin
Requires(post):	plymouth-scripts  = %{version}-%{release}
Requires:	plymouth-plugin-tribar = %{version}-%{release}

%description theme-tribar
This package contains the "Tribar" boot splash theme for Plymouth.

%prep
%setup -q
%apply_patches

%if %{snapshot}
sh ./autogen.sh
make distclean
%endif
libtoolize --copy --force
autoreconf -fi

%build
export CONFIGURE_TOP=`pwd`
%global optflags %{optflags} -Os

%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%configure CC="%{uclibc_cc}" \
	CFLAGS="%{uclibc_cflags}" \
	LDFLAGS="%{ldflags} -lz" \
	--prefix=%{uclibc_root}%{_prefix} \
	--libdir="%{uclibc_root}%{_libdir}" \
	--bindir="%{uclibc_root}%{plymouthclient_execdir}" \
	--sbindir="%{uclibc_root}%{plymouthdaemon_execdir}" \
	--disable-tests \
	--with-logo=%{_datadir}/plymouth/themes/OpenMandriva/openmandriva-logo.png \
	--with-background-start-color-stop=0x0073B3 \
	--with-background-end-color-stop=0x00457E \
	--with-background-color=0x3391cd \
	--disable-gdm-transition \
	--without-gdm-autostart-file \
	--without-rhgb-compat-link \
	--with-system-root-install \
	--enable-systemd-integration \
	--enable-drm-renderer \
	--enable-pango \
%if %mdvver >= 201200
	--with-release-file=/etc/os-release \
%else
	--with-release-file=/etc/mandriva-release \
%endif
	--with-log-viewer

# We don't build these for uclibc since they link against a lot of libraries
# that we don't provide any uclibc linked version of
sed -e 's#viewer##g' -i src/Makefile
sed -e 's#label##g' -i src/plugins/controls/Makefile
%make
popd
%endif

mkdir -p system
pushd system
%configure2_5x \
	--disable-static \
	--disable-tests \
	--with-logo=%{_datadir}/plymouth/themes/OpenMandriva/openmandriva-logo.png \
	--with-background-start-color-stop=0x0073B3 \
	--with-background-end-color-stop=0x00457E \
	--with-background-color=0x3391cd \
	--disable-gdm-transition \
	--without-gdm-autostart-file \
	--without-rhgb-compat-link \
	--with-system-root-install \
	--enable-systemd-integration \
	--enable-drm-renderer \
	--enable-pango \
%if %mdvver >= 201200
	--with-release-file=/etc/os-release \
%else
	--with-release-file=/etc/mandriva-release \
%endif
	--with-log-viewer


%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc plymouthdaemondir=%{uclibc_root}%{plymouthdaemon_execdir} plymouthclientdir=%{uclibc_root}%{plymouthclient_execdir}
rm -rf %{buildroot}%{uclibc_root}{%{_includedir},%{_datadir},%{_libdir}/pkgconfig,%{_libexecdir},%{plymouthdaemon_execdir}/plymouth-set-default-theme}
%endif
%makeinstall_std -C system

# Temporary symlink until rc.sysinit is fixed
(cd %{buildroot}%{_bindir}; ln -s ../../bin/plymouth)
touch %{buildroot}%{_datadir}/plymouth/themes/default.plymouth

mkdir -p %{buildroot}%{_localstatedir}/lib/plymouth
cp %{SOURCE1} %{buildroot}%{_datadir}/plymouth/default-boot-duration
touch %{buildroot}%{_localstatedir}/lib/plymouth/{boot,shutdown}-duration

# Add charge
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/charge
cp %{SOURCE2} %{buildroot}%{_datadir}/plymouth/themes/charge
cp %{buildroot}%{_datadir}/plymouth/themes/glow/{box,bullet,entry,lock}.png %{buildroot}%{_datadir}/plymouth/themes/charge

find %{buildroot} -name \*.a -delete -o -name \*.la -delete

%post
[ -f %{_localstatedir}/lib/plymouth/boot-duration ] || cp -f %{_datadir}/plymouth/default-boot-duration %{_localstatedir}/lib/plymouth/boot-duration
if [ "x$DURING_INSTALL" = "x" ]; then
  if [ $1 -eq 1 ]; then
   %{_libexecdir}/plymouth/plymouth-update-initrd
  fi
fi

%postun
if [ $1 -eq 0 ]; then
    rm -f %{_libdir}/plymouth/default.so
fi

%define theme_scripts() \
%post -n %{name}-theme-%{1} \
if [ -x %{_sbindir}/plymouth-set-default-theme ]; then \
  export LIB=%{_lib} \
  if [ $1 -eq 1 ]; then \
      %{_sbindir}/plymouth-set-default-theme --rebuild-initrd %{1} \
  else \
      THEME=$(%{_sbindir}/plymouth-set-default-theme) \
      if [ "$THEME" == "text" -o "$THEME" == "%{1}" ]; then \
          %{_sbindir}/plymouth-set-default-theme --rebuild-initrd %{1} \
      fi \
  fi \
fi \
\
%postun -n %{name}-theme-%{1} \
export LIB=%{_lib} \
if [ $1 -eq 0 -a -x %{_sbindir}/plymouth-set-default-theme ]; then \
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "%{1}" ]; then \
        %{_sbindir}/plymouth-set-default-theme --reset --rebuild-initrd \
    fi \
fi \

%theme_scripts spinfinity
%theme_scripts fade-in
%theme_scripts solar
%theme_scripts charge
%theme_scripts glow
%theme_scripts script

%files
%doc AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/plymouth
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_libdir}/plymouth
%{_datadir}/plymouth/default-boot-duration
%dir %{_localstatedir}/lib/plymouth
%{plymouthdaemon_execdir}/plymouthd
%{plymouthclient_execdir}/plymouth
%{_bindir}/plymouth
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
/lib/systemd/system/*plymouth*.service
/lib/systemd/system/systemd-*.path
/lib/systemd/system/*.wants/plymouth-*.service
%dir %{_libdir}/plymouth/renderers
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*
%ghost %{_datadir}/plymouth/themes/default.plymouth
%{_datadir}/plymouth/plymouthd.defaults
%{_datadir}/plymouth/themes/details
%{_datadir}/plymouth/themes/text
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
%ghost %{_localstatedir}/lib/plymouth/shutdown-duration
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%{_mandir}/man8/*
%if %{with uclibc}
%{uclibc_root}%{plymouthdaemon_execdir}/plymouthd
%{uclibc_root}%{plymouthclient_execdir}/plymouth
%{uclibc_root}%{_libdir}/plymouth/details.so
%{uclibc_root}%{_libdir}/plymouth/text.so
%endif

%files -n %{libply}
%{plymouth_libdir}/libply.so.%{major}*

%files -n %{libply_boot_client}
%{_libdir}/libply-boot-client.so.%{major}*

%files -n %{libply_splash_graphics}
%{_libdir}/libply-splash-graphics.so.%{major}*

%files -n %{libply_splash_core}
/%{_lib}/libply-splash-core.so.%{major}*

%if %{with uclibc}
%files -n uclibc-%{libname}
%dir %{uclibc_root}%{_libdir}/plymouth
%{uclibc_root}%{plymouth_libdir}/libply.so*
%{uclibc_root}%{_libdir}/libply-boot-client.so*
%{uclibc_root}%{_libdir}/libply-splash-graphics.so*
%endif

%files -n %{devname}
%{plymouth_libdir}/libply.so
%{_libdir}/libply-boot-client.so
%{_libdir}/libply-splash-graphics.so
%{_libdir}/plymouth/renderers/x11*
/%{_lib}/libply-splash-core.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/plymouth-1

%files scripts
%{_sbindir}/plymouth-set-default-theme
%{_libexecdir}/plymouth

%files utils
%{_bindir}/plymouth-log-viewer

%files plugin-label
%{_libdir}/plymouth/label.so

%files plugin-fade-throbber
%{_libdir}/plymouth/fade-throbber.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/plymouth/fade-throbber.so
%endif

%files theme-fade-in
%{_datadir}/plymouth/themes/fade-in

%files plugin-throbgress
%{_libdir}/plymouth/throbgress.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/plymouth/throbgress.so
%endif

%files plugin-script
%{_libdir}/plymouth/script.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/plymouth/script.so
%endif

%files theme-script
%{_datadir}/plymouth/themes/script

%files theme-spinfinity
%{_datadir}/plymouth/themes/spinfinity

%files theme-spinner
%{_datadir}/plymouth/themes/spinner

%files plugin-space-flares
%{_libdir}/plymouth/space-flares.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/plymouth/space-flares.so
%endif

%files theme-solar
%{_datadir}/plymouth/themes/solar

%files plugin-two-step
%{_libdir}/plymouth/two-step.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/plymouth/two-step.so
%endif

%files plugin-tribar
%{_libdir}/plymouth/tribar.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/plymouth/tribar.so
%endif

%files theme-tribar
%{_datadir}/plymouth/themes/tribar

%files theme-charge
%{_datadir}/plymouth/themes/charge

%files theme-glow
%{_datadir}/plymouth/themes/glow

%files system-theme

