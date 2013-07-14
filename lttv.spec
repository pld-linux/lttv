#
# Conditional build:
%bcond_without	glpk	# trace synchronization accuracy calculation
%bcond_without	java	# JNI interface
#
Summary:	Linux Trace Toolkit Viewer
Summary(pl.UTF-8):	Linux Trace Toolkit Viewer - przeglądarka dla LTT
Name:		lttv
Version:	1.5
%define	subver	beta1
Release:	0.%{subver}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://lttng.org/files/packages/%{name}-%{version}-%{subver}.tar.bz2
# Source0-md5:	f89042bb64bf390f9b6814fa4abb6d85
URL:		http://lttng.org/
BuildRequires:	babeltrace-devel >= 1.1.0
%{?with_glpk:BuildRequires:	glpk-devel}
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
%{?with_java:BuildRequires:	jdk}
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
Requires:	babeltrace >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the trace viewing tools for the new Linux Trace
Toolkit trace format.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do oglądania śladów dla nowego formatu
Linux Trace Toolkitu.

%package gui
Summary:	GTK+ GUI for LTTV
Summary(pl.UTF-8):	Graficzny interfejs GTK+ do LTTV
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.0

%description gui
GTK+ GUI for LTTV.

%description gui -l pl.UTF-8
Graficzny interfejs GTK+ do LTTV.

%package devel
Summary:	Header files for LTTV plugins
Summary(pl.UTF-8):	Pliki nagłówkowe dla wtyczek LTTV
Group:		Development/Libraries
Requires:	glib2-devel >= 2.0.0
# for lttvwindow
Requires:	gtk+2-devel >= 2:2.4.0

%description devel
Header files for LTTV plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla wtyczek LTTV.

%prep
%setup -q -n %{name}-%{version}-%{subver}

%build
#CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--disable-silent-rules \
	--disable-static \
	%{?with_java:--with-jni-interface} \
	%{?with_glpk:--with-trace-sync}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lttv/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README LTTngManual.html
%attr(755,root,root) %{_bindir}/lttv
%attr(755,root,root) %{_bindir}/lttv.real
%dir %{_libdir}/lttv
%dir %{_libdir}/lttv/plugins

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lttv-gui
# note: probably some of them don't require GUI, but all are linked with GUI libs
%attr(755,root,root) %{_libdir}/lttv/plugins/libbatchAnalysis.so
%attr(755,root,root) %{_libdir}/lttv/plugins/libguicontrolflow.so
%attr(755,root,root) %{_libdir}/lttv/plugins/libguievents.so
%attr(755,root,root) %{_libdir}/lttv/plugins/libguihistogram.so
%attr(755,root,root) %{_libdir}/lttv/plugins/liblttvwindow.so
%attr(755,root,root) %{_libdir}/lttv/plugins/libresourceview.so
%attr(755,root,root) %{_libdir}/lttv/plugins/libtextDump.so
%{_pixmapsdir}/lttv

%files devel
%defattr(644,root,root,755)
%{_includedir}/lttv
%{_includedir}/lttvwindow
