Name:           ea-nginx-gzip
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 2
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Enable gzip config for ea-nginx
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       ea-nginx

Provides:       ea-nginx-compression
Conflicts:      ea-nginx-compression

Source0:        gzip.conf

%description
Makes ea-nginx configure gzip compression.

per NGINX (http://nginx.org/en/docs/http/ngx_http_gzip_module.html):
    - When using the SSL/TLS protocol, compressed responses may be subject to BREACH attacks.
    - https://en.wikipedia.org/wiki/BREACH
The best mitigation (besides not using compression at all) is:
    1. Not sending sensitive data as part of your HTTP response
    2. Use strict samesite cookies
       - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite

If that is not an acceptable risk please uninstall `ea-nginx-gzip`

%build
echo "Nothing to build"

%install
mkdir -p %{buildroot}/etc/nginx/conf.d
install %{SOURCE0} %{buildroot}/etc/nginx/conf.d/gzip.conf

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%config(noreplace) /etc/nginx/conf.d/gzip.conf

%changelog
* Thu Feb 24 2022 Dan Muey <dan@cpanel.net> - 1.0-2
- ZC-9757: changes for co-existence w/ brotli compression

* Tue Feb 01 2022 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9697: Initial version
