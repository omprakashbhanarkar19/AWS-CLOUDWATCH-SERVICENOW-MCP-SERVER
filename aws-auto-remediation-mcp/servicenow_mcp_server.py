
import requests
from config import SN_INSTANCE, SN_USER, SN_PASSWORD



BASE_URL = f"https://{SN_INSTANCE}.service-now.com/api/now/table/incident"
HEADERS = {"Content-Type": "application/json"}

def create_incident(description):
    """
    Create a new ServiceNow incident with a description
    """
    payload = {
        "short_description": description,
        "category": "inquiry",
        "urgency": "1",
        "impact": "1"
    }

    r = requests.post(
        BASE_URL,
        auth=(SN_USER, SN_PASSWORD),
        headers=HEADERS,
        json=payload
    )

    print("🔍 ServiceNow Status Code:", r.status_code)
    print("🔍 ServiceNow Response:", r.text)

    data = r.json()
    if "result" not in data:
        raise Exception(f"ServiceNow Error: {data}")

    return data["result"]["sys_id"]

def resolve_incident(sys_id):
    print("➡️ Moving incident to In Progress")

    # STEP 1: Move to In Progress
    r1 = requests.patch(
        f"{BASE_URL}/{sys_id}",
        auth=(SN_USER, SN_PASSWORD),
        headers=HEADERS,
        json={"state": "2", "incident_state": "2"}
    )

    print("🔍 In Progress Status:", r1.status_code)
    print("🔍 In Progress Response:", r1.text)

    print("➡️ Resolving incident")

    # STEP 2: Resolve with mandatory fields
    payload = {
        "state": "6",
        "incident_state": "6",
        "close_code": "solved permanently",
        "close_notes": "Auto-remediation completed. EC2 instance restarted successfully."
    }

    r2 = requests.patch(
        f"{BASE_URL}/{sys_id}",
        auth=(SN_USER, SN_PASSWORD),
        headers=HEADERS,
        json=payload
    )

    print("🔍 Resolve Status:", r2.status_code)
    print("🔍 Resolve Response:", r2.text)

    return r2