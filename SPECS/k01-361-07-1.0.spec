Name: k01-361-07 

Version: 1.0 

Release: 1%{?dist} 

Summary: Программа студента Кузнецовой Ксении группы k01-361-07   

Group: Testing 

License: GPL 

URL: http://www.lug.mephist.ru 

Source0:  %{name}-%{version}.tar.gz 

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)  

BuildRequires: /bin/rm, /bin/mkdir, /bin/cp 

Requires: /bin/bash, /bin/date 

%description 

A test package 

%prep 

%setup -q 

%build 

#configure 

#make %{&_smp_mflags} 

%install 

rm -rf $RPM_BUILD_ROOT 

#make install DESTDIR=$RPM_BUILD_ROOT 

mkdir -p $RPM_BUILD_ROOT/usr/local/bin 

cp k01-361-07 $RPM_BUILD_ROOT/usr/local/bin 

%clean 

rm -rf $RPM_BUILD_ROOT 

%files 

%defattr(-,root,root,-) 

#%doc 

%attr(0755,root,root)/usr/local/bin/k01-361-07 

%changelog 

* Sun Dec 14 2014 Кузнецова 

- Added /usr/local/bin/k01-361-07 


