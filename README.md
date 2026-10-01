# Python Port Scanner

A simple TCP port scanner written in Python using the built-in `socket` library. Built as a learning project while studying BSc Cybersecurity at Aston University.

## What it does
- Scans a host for open TCP ports across a range you choose
- Looks up the common service name for each open port
- Validates input and handles unresolvable hosts

## Usage
```
python scanner.py
```
Press Enter at each prompt to scan your own machine (127.0.0.1) on ports 1-1024.

## Example output
```
Scanning 127.0.0.1 (127.0.0.1) ports 1-1024
Started: 2026-10-01 23:32:25

[OPEN] 135/tcp  epmap
[OPEN] 445/tcp  microsoft-ds

Done. 2 open port(s) found.
```
Scan of a local Windows machine: ports 135 (RPC endpoint mapper) and 445 (SMB) are open by default.

## How it works
For each port, the scanner opens a TCP socket with a short timeout and calls `connect_ex()`. A return value of 0 means the connection succeeded, so the port is open.

## Possible improvements
- Use threading to scan ports in parallel
- Add command-line arguments instead of prompts
- Save results to a file

## Legal and ethical note
Only scan systems you own or have explicit permission to scan. Unauthorised scanning may be illegal.
