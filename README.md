# nginx-log-analyzer

A Python script that reads an NGINX access log and prints a report:
status codes, 5xx error rate, top IPs, top paths, and requests per hour.
Bad lines are skipped instead of crashing the program.

Plain Python 3, no external libraries. Learning project, work in progress.

 
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

Set the log file path at the top of `main.py`.

## Files

- `main.py` – starts the program
- `Parsers.py` – splits each line into fields
- `Analyzers.py` – counts and calculates stats
- `Reporter.py` – prints the report
- `Models.py` – holds one parsed line
