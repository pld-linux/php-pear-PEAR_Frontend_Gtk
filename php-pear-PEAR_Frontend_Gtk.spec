%define		_class		PEAR
%define		_subclass	Frontend
%define		_pearname	%{_class}_%{_subclass}_Gtk
Summary:	%{_class}_%{_subclass} - Gtk (Desktop) PEAR Package Manager
Summary(pl):	%{_class}_%{_subclass} - Desktop w Gtk dla managera pakietów PEAR
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
Requires:	php-gtk
Requires:	php-pear
Requires:	php-pear-PEAR
Provides:	pear(Frontend)
Provides:	pear(%{_class}_%{_subclass}_Gtk)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		php_pear_dir	/usr/share/pear/

%description
Desktop Interface to the PEAR Package Manager.

%description -l pl
Desktop w Gtk dla managera pakietów PEAR.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/xpm

install %{_pearname}-%{version}/Gtk.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Gtk/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Gtk
install %{_pearname}-%{version}/Gtk/*.glade $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Gtk
install %{_pearname}-%{version}/Gtk/xpm/*.xpm $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Gtk
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Gtk/xpm
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/*.glade
%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/xpm/*
