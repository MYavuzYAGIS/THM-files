❯ nikto -h 10.10.140.69 -port 10000
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.140.69
+ Target Hostname:    10.10.140.69
+ Target Port:        10000
+ Start Time:         2021-10-27 00:42:49 (GMT3)
---------------------------------------------------------------------------
+ Server: SimpleHTTP/0.6 Python/2.7.3
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Python/2.7.3 appears to be outdated (current is at least 2.7.5)
+ SimpleHTTP/0.6 appears to be outdated (current is at least 1.2)
