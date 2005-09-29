%include	/usr/lib/rpm/macros.php
%define		_class		PEAR
%define		_subclass	Frontend
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Gtk

Summary:	%{_pearname} - GTK+ (Desktop) PEAR Package Manager
Summary(pl):	%{_pearname} - Desktop w GTK+ dla managera pakietów PEAR
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2ed87947a9fe6d09a11c0e9fc797d1cf
URL:		http://pear.php.net/package/PEAR_Frontend_Gtk/
Requires:	php4-gtk
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Desktop Interface to the PEAR Package Manager.

In PEAR status of this package is: %{_status}.

%description -l pl
Desktop w GTK+ dla managera pakietów PEAR.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Gtk
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Gtk/xpm
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/*.glade
%{php_pear_dir}/%{_class}/%{_subclass}/Gtk/xpm/*
