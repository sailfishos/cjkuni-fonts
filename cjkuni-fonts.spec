%define fontname	cjkuni-fonts
%define gsdir           %{_datadir}/ghostscript/conf.d
%define catalogue       %{_sysconfdir}/X11/fontpath.d

%define umingbuilddir   %{fontname}-uming-fonts-%{version}
%define ukaibuilddir    %{fontname}-ukai-fonts-%{version}


Name:        cjkuni-fonts
Version:     0.2.20080216.1
Release:     20
Summary:     Chinese Unicode TrueType fonts in Ming and Kai face
License:     Arphic
Group:       User Interface/X
URL:         http://www.freedesktop.org/wiki/Software/CJKUnifonts

Source1:    http://ftp.debian.org/debian/pool/main/t/ttf-arphic-uming/ttf-arphic-uming_%{version}.orig.tar.gz
Source2:    http://ftp.debian.org/debian/pool/main/t/ttf-arphic-ukai/ttf-arphic-ukai_%{version}.orig.tar.gz
Source3:    FAPIcidfmap.zh_TW
Source4:    FAPIcidfmap.zh_CN
Source5:    cidfmap.zh_TW
Source6:    cidfmap.zh_CN
Source7:    CIDFnmap.zh_TW
Source8:    CIDFnmap.zh_CN
Patch1:     cjkunifonts-0.2.20080216.1-2.patch
Patch3:     cjkuni-fonts-0.2.20080216.1-19.patch
Patch4:     64-ttf-arphic-uming.conf.patch

Provides:   ttf-arphic-ukai
Provides:   ttf-arphic-uming
Provides:   scalable-font-zh-TW
Provides:   scalable-font-zh-HK
Provides:   scalable-font-zh-CN
Provides:   scalable-font-zh-SG
Provides:   scalable-font-zh-MO 

BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils, ttmkfdir

%description
CJK Unifonts are Unicode TrueType fonts derived from original fonts made
available by Arphic Technology under "Arphic Public License" and extended by
the CJK Unifonts project.



%files 
%defattr(-,root,root,-)
%doc ../%{umingbuilddir}/license
%doc ../%{umingbuilddir}/CONTRIBUTERS
#%doc ../%{umingbuilddir}/Font_Comparison_ShanHeiSun_UMing.odt
#%doc ../%{umingbuilddir}/Font_Comparison_ShanHeiSun_UMing.pdf
%doc ../%{umingbuilddir}/FONTLOG
#%doc ../%{umingbuilddir}/INSTALL
#%doc ../%{umingbuilddir}/KNOWN_ISSUES
#%doc ../%{umingbuilddir}/NEWS
%doc ../%{umingbuilddir}/README
#%doc ../%{umingbuilddir}/TODO
%doc ../%{ukaibuilddir}/license
%doc ../%{ukaibuilddir}/CONTRIBUTERS
#%doc ../%{ukaibuilddir}/Font_Comparison_ZenKai_UKai.odt
#%doc ../%{ukaibuilddir}/Font_Comparison_ZenKai_UKai.pdf
%doc ../%{ukaibuilddir}/FONTLOG
#%doc ../%{ukaibuilddir}/INSTALL
#%doc ../%{ukaibuilddir}/KNOWN_ISSUES
#%doc ../%{ukaibuilddir}/NEWS
%doc ../%{ukaibuilddir}/README
%doc ../%{ukaibuilddir}/TODO
%dir %{_fontdir}
%{gsdir}/FAPIcidfmap.zh_TW
%{gsdir}/FAPIcidfmap.zh_CN
%{gsdir}/cidfmap.zh_TW
%{gsdir}/cidfmap.zh_CN
%{gsdir}/CIDFnmap.zh_TW
%{gsdir}/CIDFnmap.zh_CN
%verify(not md5 size mtime) %{_fontdir}/fonts.dir
%verify(not md5 size mtime) %{_fontdir}/fonts.scale
%{catalogue}/%{name}
%verify(not md5 size mtime) %{_datadir}/fonts/zh_CN/TrueType/zysong.ttf
%verify(not md5 size mtime) %{_datadir}/fonts/zh_TW/TrueType/bsmi00lp.ttf
/etc/fonts/conf.d/25-ttf-arphic-ukai-render.conf
/etc/fonts/conf.d/25-ttf-arphic-uming-bitmaps.conf
/etc/fonts/conf.d/25-ttf-arphic-uming-render.conf
/etc/fonts/conf.d/35-ttf-arphic-ukai-aliases.conf
/etc/fonts/conf.d/35-ttf-arphic-uming-aliases.conf
/etc/fonts/conf.d/41-ttf-arphic-ukai.conf
/etc/fonts/conf.d/41-ttf-arphic-uming.conf
/etc/fonts/conf.d/64-ttf-arphic-uming.conf
/etc/fonts/conf.d/75-ttf-arphic-ukai-select.conf
/etc/fonts/conf.d/90-ttf-arphic-ukai-embolden.conf
/etc/fonts/conf.d/90-ttf-arphic-uming-embolden.conf
/usr/share/fontconfig/conf.avail/25-ttf-arphic-ukai-render.conf
/usr/share/fontconfig/conf.avail/25-ttf-arphic-uming-bitmaps.conf
/usr/share/fontconfig/conf.avail/25-ttf-arphic-uming-render.conf
/usr/share/fontconfig/conf.avail/35-ttf-arphic-ukai-aliases.conf
/usr/share/fontconfig/conf.avail/35-ttf-arphic-uming-aliases.conf
/usr/share/fontconfig/conf.avail/41-ttf-arphic-ukai.conf
/usr/share/fontconfig/conf.avail/41-ttf-arphic-uming.conf
/usr/share/fontconfig/conf.avail/64-ttf-arphic-uming.conf
/usr/share/fontconfig/conf.avail/75-ttf-arphic-ukai-select.conf
/usr/share/fontconfig/conf.avail/90-ttf-arphic-ukai-embolden.conf
/usr/share/fontconfig/conf.avail/90-ttf-arphic-uming-embolden.conf
/usr/share/fonts/cjkuni-fonts/ukai.ttc
/usr/share/fonts/cjkuni-fonts/uming.ttc


%prep
%setup -q -c -T -a1 -n %{umingbuilddir}
%patch1 -p1 -b .1-rhbz466667
%patch3 -p1 -b .3-rhbz459680
%patch4 -p1 -b .uming
%setup -q -c -T -a2 -n %{ukaibuilddir}

%build
%{nil}

%install
%__rm -rf %{buildroot}

# *.ttc(ttf)
%__install -m 0755 -d %{buildroot}%{_fontdir}
%__install -m 0644 ../%{umingbuilddir}/uming.ttc %{buildroot}%{_fontdir}/
%__install -m 0644 ../%{ukaibuilddir}/ukai.ttc %{buildroot}%{_fontdir}/

# fonts.{scale,dir}
%{_bindir}/ttmkfdir -d %{buildroot}%{_fontdir} \
    -o %{buildroot}%{_fontdir}/fonts.scale
%{_bindir}/mkfontdir %{buildroot}%{_fontdir}

# *.conf
%__install -m 0755 -d %{buildroot}%{_fontconfig_templatedir}
%__install -m 0755 -d %{buildroot}%{_fontconfig_confdir}
cd ../%{umingbuilddir}
for fconf in `ls *-ttf-arphic-uming*.conf`
do
    %__install -m 0644 $fconf %{buildroot}%{_fontconfig_templatedir}/
    %__ln_s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
cd ../%{ukaibuilddir}
for fconf in `ls *-ttf-arphic-ukai*.conf`
do
    %__install -m 0644 $fconf %{buildroot}%{_fontconfig_templatedir}/
    %__ln_s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
cd -

# ghostscript
%__install -m 0755 -d %{buildroot}%{gsdir}
%__install -m 0644 %{SOURCE3} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE4} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE5} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE6} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE7} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE8} %{buildroot}%{gsdir}/

# catalogue
%__install -m 0755 -d %{buildroot}%{catalogue}
%__ln_s %{_fontdir} %{buildroot}%{catalogue}/%{name}

# backward compat to obsoleted ttf
%__install -m 0755 -d %{buildroot}%{_datadir}/fonts/zh_CN/TrueType
%__install -m 0755 -d %{buildroot}%{_datadir}/fonts/zh_TW/TrueType
%__ln_s %{_fontdir}/uming.ttc \
    %{buildroot}%{_datadir}/fonts/zh_CN/TrueType/zysong.ttf
%__ln_s %{_fontdir}/uming.ttc \
    %{buildroot}%{_datadir}/fonts/zh_TW/TrueType/bsmi00lp.ttf

%clean
%__rm -fr %{buildroot}

