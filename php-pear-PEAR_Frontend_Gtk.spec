%define		_class		PEAR
%define		_subclass	Frontend
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Gtk

Summary:	%{_pearname} - GTK+ (Desktop) PEAR Package Manager
Summary(pl):	%{_pearname} - Desktop w GTK+ dla managera pakiet�w PEAR
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8ea4b105ad2af5a6726515f7d341e168
URL:		http://pear.php.net/package/PEAR_Frontend_Gtk/
Requires:	php-gtk
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		php_pear_dir	/usr/share/pear/

%description
Desktop Interface to the PEAR Package Manager.

In PEAR status of this package is: %{_status}.

%description -l pl
Desktop w GTK+ dla managera pakiet�w PEAR.

Ta klasa ma w PEAR status: %{_status}.

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
