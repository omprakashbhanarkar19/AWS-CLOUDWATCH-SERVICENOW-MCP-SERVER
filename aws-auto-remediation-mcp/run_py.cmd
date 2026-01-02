@echo off 

:loop
echo starting auto remediation.....
python orchestrator_mcp_server.py
echo script crashed, Restaring in 10 secounds...
timeout/t 30
goto loop

