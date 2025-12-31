import boto3
from config import AWS_REGION

ec2 = boto3.client("ec2", region_name=AWS_REGION)

def restart_instance(instance_id):
    print(f"🔁 Restarting EC2 Instance: {instance_id}")
    ec2.reboot_instances(InstanceIds=[instance_id])

def get_instance_name(instance_id):
    """
    Fetch EC2 Name tag
    """
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])

        reservations = response.get("Reservations", [])
        for res in reservations:
            for inst in res.get("Instances", []):
                for tag in inst.get("Tags", []):
                    if tag["Key"] == "Name":
                        return tag["Value"]

        return "N/A"

    except Exception as e:
        print(f"❌ Error fetching instance name: {e}")
        return "N/A"