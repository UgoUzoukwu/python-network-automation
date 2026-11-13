# Python Network Automation

A small Python script for a common help desk task: check which hosts on a list respond to ping and save the result.

## What it does

- Reads IP addresses or hostnames from a text file, one per line
- Pings each one once (uses the right ping flag for Windows, macOS or Linux)
- Writes `Success` or `Failure` for each host to a report file

## Files

- `ping_ips.py`: the script
- `ips.txt`: sample input

## Requirements

Python 3.7 or later. No third-party packages.

## Usage

```bash
git clone https://github.com/UgoUzoukwu/python-network-automation.git
cd python-network-automation
python ping_ips.py                       # reads ips.txt, writes ping_results.txt
python ping_ips.py hosts.txt -o out.txt  # custom input and output files
```

Example report:

```
8.8.8.8: Success
192.0.2.10: Failure
```

## Ideas for later

- Ping hosts in parallel so long lists finish faster
- Add a timestamp and response time to each line
