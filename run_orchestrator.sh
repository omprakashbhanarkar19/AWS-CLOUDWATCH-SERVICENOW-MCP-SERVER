#!/usr/bin/env bash
set -u  # treat unset variables as an error

# Change to your project directory (edit this path)
cd /home/ec2-user/mcp-server/ || { echo "Directory not found"; exit 1; }

# Optional: use a virtual environment (comment out if not using venv)
# python3.10 -m venv .venv
# source .venv/bin/activate

while true; do
  echo "$(date '+%Y-%m-%d %H:%M:%S') starting auto remediation....."
  # Use python3.10 explicitly if you installed it
  python orchestrator_mcp_server.py
  exit_code=$?
  echo "$(date '+%Y-%m-%d %H:%M:%S') script exited with code ${exit_code}. Restarting in 50 seconds..."
  sleep 50
done
