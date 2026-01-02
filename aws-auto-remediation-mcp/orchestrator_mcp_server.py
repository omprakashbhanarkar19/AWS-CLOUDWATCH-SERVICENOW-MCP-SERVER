# from cloudwatch_mcp_server import get_metric
# from aws_mcp_server import restart_instance, get_instance_name
# from servicenow_mcp_server import create_incident, resolve_incident
# from config import CPU_THRESHOLD, MEM_THRESHOLD

# INSTANCE_ID = "i-07d743b1d544c8215"

# def main():
#     cpu = get_metric(INSTANCE_ID, "CPUUtilization")
#     mem = get_metric(INSTANCE_ID, "mem_used_percent")
#     instance_name = get_instance_name(INSTANCE_ID)
    
#     #print(f"📊 CPU={cpu:.2f}% | MEM={mem:.2f}%")

#     print(
#         f"{instance_name} ({INSTANCE_ID}) | "
#         f"CPU={cpu:.2f}% | MEM={mem:.2f}%"
#     )

#     if cpu >= CPU_THRESHOLD or mem >= MEM_THRESHOLD:
#         print("🚨 Threshold exceeded")

#         inc = create_incident(f"High CPU/MEM on {INSTANCE_ID}")
#         print(f"🧾 Incident created: {inc}")

#         restart_instance(INSTANCE_ID)

#         resolve_incident(inc)
#         print("✅ Incident resolved")

# if __name__ == "__main__":
#     main()


from cloudwatch_mcp_server import get_metric
from aws_mcp_server import restart_instance, get_instance_name
from servicenow_mcp_server import create_incident, resolve_incident
from config import CPU_THRESHOLD, MEM_THRESHOLD

#INSTANCE_ID = "i-07d743b1d544c8215"

INSTANCE_IDS = [
    "i-0e7d08890e5c24c61"
]

def main():
    #instance_name = get_instance_name(INSTANCE_ID)
    for instance_id in INSTANCE_IDS:
        print("\n-----------------------------------")
        
        instance_name = get_instance_name(instance_id)

    cpu = get_metric(instance_id, "CPUUtilization")
    mem = get_metric(instance_id, "mem_used_percent")

    print(f"📊 {instance_name} ({instance_id}) | CPU={cpu:.2f}% | MEM={mem:.2f}%")

    if cpu >= CPU_THRESHOLD or mem >= MEM_THRESHOLD:
        print("🚨 Threshold exceeded")

        # Check if incident already exists (optional)
        # Here we always create new incident for simplicity
        description = (
            f"High CPU/MEM detected\n"
            f"Instance Name: {instance_name}\n"
            f"Instance ID: {instance_id}\n"
            f"CPU: {cpu:.2f}% | MEM: {mem:.2f}%"
        )

        incident_sys_id = create_incident(description)
        print(f"🧾 Incident created: {incident_sys_id}")

        # Restart EC2
        restart_instance(instance_id)

        # Update existing incident to Resolved
        resolve_incident(incident_sys_id)
        print("✅ Incident resolved")

if __name__ == "__main__":
    main()
