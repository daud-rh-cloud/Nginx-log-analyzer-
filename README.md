nginx-log-analyzer

A small Python tool that reads an NGINX access log and prints a report: status codes, 5xx error rate, top IPs, top paths, and requests per hour. Lines that can't be parsed are skipped and listed instead of crashing the program.

Plain Python 3, no external libraries.

Status: learning project, work in progress.

Example input

Each line is one request in NGINX's combined log format:

192.168.1.10 - - [05/Oct/2026:13:00:01 +0200] "GET /api/users HTTP/1.1" 200 512 "-" "curl/8.4.0"
Example output
=== logsentry report: big.log ===
Status codes:
200     26
404     5
...
5xx Error rate: 12.50%

Top IPs:
198.51.100.23   10
192.0.2.88      8
...

Requests per hour:
07/Oct/2026:08    1
07/Oct/2026:09    21
...
