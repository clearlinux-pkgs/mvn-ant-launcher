#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-ant-launcher
Version  : 1.9.3
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.jar
Source0  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.jar
Source1  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.8.1/ant-launcher-1.8.1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.8.1/ant-launcher-1.8.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.8.2/ant-launcher-1.8.2.jar
Source4  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.8.2/ant-launcher-1.8.2.pom
Source5  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.pom
Source6  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.9.4/ant-launcher-1.9.4.jar
Source7  : https://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.9.4/ant-launcher-1.9.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-ant-launcher-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-ant-launcher package.
Group: Data

%description data
data components for the mvn-ant-launcher package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.1/ant-launcher-1.8.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.1/ant-launcher-1.8.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.2/ant-launcher-1.8.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.2/ant-launcher-1.8.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.4/ant-launcher-1.9.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.4/ant-launcher-1.9.4.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.1/ant-launcher-1.8.1.jar
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.1/ant-launcher-1.8.1.pom
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.2/ant-launcher-1.8.2.jar
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.8.2/ant-launcher-1.8.2.pom
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.jar
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.3/ant-launcher-1.9.3.pom
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.4/ant-launcher-1.9.4.jar
/usr/share/java/.m2/repository/org/apache/ant/ant-launcher/1.9.4/ant-launcher-1.9.4.pom
