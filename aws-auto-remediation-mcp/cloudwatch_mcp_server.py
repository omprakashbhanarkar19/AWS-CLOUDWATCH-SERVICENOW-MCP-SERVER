import boto3
from datetime import datetime, timedelta
from config import AWS_REGION

cw = boto3.client("cloudwatch", region_name=AWS_REGION)

def get_metric(instance_id, metric):
    response = cw.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName=metric,
        Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
        StartTime=datetime.utcnow() - timedelta(minutes=10),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=["Average"]
    )
    return response["Datapoints"][-1]["Average"] if response["Datapoints"] else 0
