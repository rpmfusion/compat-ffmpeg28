%if 0%{?rhel}
%global _without_vpx      1
%endif
%global _without_frei0r   1
%global _without_ladspa   1
%global _without_openal   1
%global _without_pulse    1
%global _without_vaapi    1
%global _without_x264     1
%global _without_x265     1

Summary:        Digital VCR and streaming server
Name:           compat-ffmpeg28
Version:        2.8.13
Release:        3%{?dist}
%if 0%{?!_without_amr:1}
License:        GPLv3+
%else
License:        GPLv2+
%endif
URL:            http://ffmpeg.org/
Source0:        %{url}/releases/ffmpeg-%{version}.tar.xz


BuildRequires:  bzip2-devel
%{?_with_celt:BuildRequires: celt-devel}
%{?_with_dirac:BuildRequires: dirac-devel}
%{?_with_faac:BuildRequires: faac-devel}
%{?_with_fdk_aac:BuildRequires: fdk-aac-devel}
BuildRequires:  freetype-devel
%{!?_without_frei0r:BuildRequires: frei0r-devel}
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
BuildRequires:  lame-devel >= 3.98.3
%{?_with_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
BuildRequires:  libass-devel
%{!?_without_cdio:BuildRequires: libcdio-paranoia-devel}
#libcrystalhd is currently broken
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
BuildRequires:  libdc1394-devel
Buildrequires:  libmodplug-devel
%{?_with_rtmp:BuildRequires: librtmp-devel}
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
%{?!_without_vpx:BuildRequires: libvpx-devel >= 0.9.1}
%ifarch %{ix86} x86_64
%{?!_without_vaapi:BuildRequires: libva-devel >= 0.31.0}
%endif
%{!?_without_amr:BuildRequires: opencore-amr-devel vo-amrwbenc-devel}
%{!?_without_openal:BuildRequires: openal-soft-devel}
%{?_with_opencl:BuildRequires: opencl-headers ocl-icd-devel}
BuildRequires:  openjpeg-devel
BuildRequires:  opus-devel
%{!?_without_pulse:BuildRequires: pulseaudio-libs-devel}
BuildRequires:  perl(Pod::Man)
BuildRequires:  schroedinger-devel
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  subversion
#BuildRequires:  texi2html
BuildRequires:  texinfo
%{!?_without_x264:BuildRequires: x264-devel >= 0.0.0-0.31}
%{!?_without_x265:BuildRequires: x265-devel}
BuildRequires:  xvidcore-devel
BuildRequires:  zlib-devel
%ifarch %{ix86} x86_64
BuildRequires:  yasm
%endif

# This package is specially usefull for firefox
# https://bugzilla.mozilla.org/show_bug.cgi?id=1435212
Supplements: firefox

# Obsoletes/Provides introduced in f28
Provides: ffmpeg-libs%{_isa} = %{version}-100
Obsoletes: ffmpeg-libs%{_isa} < %{version}-100
Provides: ffmpeg-compat%{_isa} = %{version}-100
Obsoletes: ffmpeg-compat%{_isa} < %{version}-100
Provides: compat-ffmpeg-libs%{_isa} = 1:%{version}-100
Obsoletes: compat-ffmpeg-libs%{_isa} < 1:%{version}-100


%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

!!! BIG FAT WARNING!!!
This package is made for compatibility with older components
It is not intended to be used in insecure environment.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

# Don't use the %%configure macro as this is not an autotool script
%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir}/%{name} \\\
    --mandir=%{_mandir} \\\
    --arch=%{_target_cpu} \\\
    --optflags="$RPM_OPT_FLAGS" \\\
    --extra-ldflags="$RPM_LD_FLAGS" \\\
    %{!?_without_amr:--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3} \\\
    --enable-bzlib \\\
    %{!?_with_crystalhd:--disable-crystalhd} \\\
    %{!?_without_frei0r:--enable-frei0r} \\\
    --enable-gnutls \\\
    %{!?_without_ladspa:--enable-ladspa} \\\
    --enable-libass \\\
    %{!?_without_cdio:--enable-libcdio} \\\
    %{?_with_celt:--enable-libcelt} \\\
    --enable-libdc1394 \\\
    %{?_with_dirac:--enable-libdirac} \\\
    %{?_with_faac:--enable-libfaac --enable-nonfree} \\\
    %{?_with_fdk_aac:--enable-libfdk-aac --enable-nonfree} \\\
    %{!?_with_jack:--disable-indev=jack} \\\
    --enable-libfreetype \\\
    --enable-libgsm \\\
    --enable-libmp3lame \\\
    %{?_with_nvenc:--enable-nvenc  --enable-nonfree} \\\
    %{!?_without_openal:--enable-openal} \\\
    %{?_with_opencl:--enable-opencl} \\\
    --enable-libopenjpeg \\\
    --enable-libopus \\\
    %{!?_without_pulse:--enable-libpulse} \\\
    %{?_with_rtmp:--enable-librtmp} \\\
    --enable-libschroedinger \\\
    --enable-libsoxr \\\
    --enable-libspeex \\\
    --enable-libtheora \\\
    --enable-libvorbis \\\
    --enable-libv4l2 \\\
    %{!?_without_vpx:--enable-libvpx} \\\
    %{!?_without_x264:--enable-libx264} \\\
    %{!?_without_x265:--enable-libx265} \\\
    --enable-libxvid \\\
    --enable-x11grab \\\
    --enable-avfilter \\\
    --enable-avresample \\\
    --enable-postproc \\\
    --enable-pthreads \\\
    --disable-static \\\
    --enable-shared \\\
    --enable-gpl \\\
    --disable-debug \\\
    --disable-stripping


%prep
%setup -q -n ffmpeg-%{version}

# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags $RPM_OPT_FLAGS|" configure

%build
%{ff_configure}\
    --shlibdir=%{_libdir} \
    --disable-doc \
    --disable-ffmpeg --disable-ffplay --disable-ffprobe --disable-ffserver \
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
%ifarch %{ix86} x86_64 ppc ppc64
    --enable-runtime-cpudetect \
%endif
%ifarch ppc
    --cpu=g3 \
    --enable-pic \
%endif
%ifarch ppc64
    --cpu=g5 \
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif

%make_build V=1

%install
%make_install V=1
#Alternative ffmpeg package move headers into a special directory
if ! [ %{name} == ffmpeg ] ; then
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/pkgconfig
for s in $RPM_BUILD_ROOT/%{_libdir}/*.so ; do 
  ffmpegsym=`basename ${s}`
  ffmpeglib=`readlink ${s}`
  echo "Symlink $ffmpeglib"
  ln -fs ../${ffmpeglib} \
    $RPM_BUILD_ROOT%{_libdir}/%{name}/${ffmpegsym}
done
rm -rf $RPM_BUILD_ROOT/%{_libdir}/*.so
fi

%ldconfig_scriptlets

%files
%doc COPYING.* CREDITS README.md
%{_libdir}/lib*.so.*

%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/pkgconfig
%{_libdir}/%{name}/pkgconfig/lib*.pc
%{_libdir}/%{name}/lib*.so


%changelog
* Tue Feb 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.8.13-3
- Clean uneeded dependencies
- Add supplements for firefox (until it gains ffmpeg-3.5 support)
- Add Obsoletes/Provides

* Fri Feb 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.8.13-2
- Rebase ffmpeg to compat-ffmpeg28

* Sat Sep 02 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.8.13-1
- Update to 2.8.13 (security issues)

* Wed Jun 07 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.8.12-1
- Update to 2.8.12

* Mon Feb 13 2017 Nicolas Chauvet <kwizart@gmail.com> - 2.8.11-1
- Update to 2.8.11
- enable AMR codecs by default - rfbz#4367

* Tue Dec 06 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.10-1
- Updated to 2.8.10
- Backported some .spec cleanups from rawhide

* Sun Dec 04 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.9-1
- Updated to 2.8.9

* Wed Sep 21 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.8-1
- Updated to 2.8.8

* Mon May 02 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.7-1
- Updated to 2.8.7

* Mon Feb 01 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.6-1
- Updated to 2.8.6

* Sat Jan 16 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.5-1
- Updated to 2.8.5

* Wed Dec 23 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.4-1
- Updated to 2.8.4
- Fixed Fraunhofer FDK AAC conditional build (RF # 3898)

* Sun Nov 29 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.8.3-1
- Updated to 2.8.3

* Sat Nov 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Sat Oct 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 2.8.1-1
- Update to 2.8.1

