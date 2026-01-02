Windows:
=========

AWS Configure

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python orchestrator_mcp_server.py



Impletment AWS EC2 Server
=============================

Steps:

Create a Ec2 Instance in AWS Account. 

Clone repo --> 

https://github.com/Capgemini-AdvancedAutomationCOE/Aws-Cloudwatch-ServiceNow-Mcp-server

Install python3.10

aws configure

attched IAM role into Ec2 instance full access and Cloudwatch Full access. 

yum install amazon-cloudwatch-agent.x86_64 and memory utilization agent install  -y

systemctl start amazon-cloudwatch-agent.service
systemctl enabel amazon-cloudwatch-agent.service
systemctl enable amazon-cloudwatch-agent.service

Run below script -

python orchestrator_mcp_server.py