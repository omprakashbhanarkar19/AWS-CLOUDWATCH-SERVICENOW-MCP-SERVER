"""

import requests
from config import SN_INSTANCE, SN_USER, SN_PASSWORD

BASE_URL = f"https://{SN_INSTANCE}.service-now.com/api/now/table/incident"

HEADERS = {"Content-Type": "application/json"}

def create_incident(desc):
    payload = {
        "short_description": desc,
        "category": "inquiry",
        "urgency": "1",
        "impact": "1"
    }

    r = requests.post(
        BASE_URL,
        auth=(SN_USER, SN_PASSWORD),
        headers={"Content-Type": "application/json"},
        json=payload
    )

    print("🔍 ServiceNow Status Code:", r.status_code)
    print("🔍 ServiceNow Response:", r.text)

    data = r.json()

    if "result" not in data:
        raise Exception(f"ServiceNow Error: {data}")

    return data["result"]["sys_id"]

"""

# def resolve_incident(sys_id):
#     payload = {
#         "state": "6",
#         "close_notes": "Auto resolved after EC2 restart"
#     }

# def resolve_incident(sys_id):
#     payload = {
#         "state": "6",  # Resolved
#         "close_code": "solved_permanently",
#         "close_notes": "Issue auto-remediated. EC2 instance restarted successfully."
#     }

#     r = requests.patch(
#         f"{BASE_URL}/{sys_id}",
#         auth=(SN_USER, SN_PASSWORD),
#         headers={"Content-Type": "application/json"},
#         json=payload
#     )

#     print("🔍 Resolve Status:", r.status_code)
#     print("🔍 Resolve Response:", r.text)



    # r = requests.patch(
    #     f"{BASE_URL}/{sys_id}",
    #     auth=(SN_USER, SN_PASSWORD),
    #     headers={"Content-Type": "application/json"},
    #     json=payload
    # )

    # print("🔍 Resolve Status:", r.status_code)
    # print("🔍 Resolve Response:", r.text)

# def update_incident(sys_id, payload):
#     r = requests.patch(
#         f"{BASE_URL}/{sys_id}",
#         auth=(SN_USER, SN_PASSWORD),
#         headers=HEADERS,
#         json=payload
#     )
#     print("🔍 Status:", r.status_code)
#     print("🔍 Response:", r.text)
#     return r


# def resolve_incident(sys_id):
#     # STEP 1: Move to In Progress (state = 2)
#     print("➡️ Moving incident to In Progress")
#     update_incident(sys_id, {
#         "state": "2"
#     })

#     # STEP 2: Resolve with mandatory fields
#     print("➡️ Resolving incident")
#     update_incident(sys_id, {
#         "state": "6",
#         #"close_code": "Solved (Permanently)",
#         #"close_notes": "Auto-remediation completed. EC2 instance restarted."
#     })


# def resolve_incident(sys_id):
#     payload = {
#         # BOTH state fields (very important)
#         "state": "6",
#         "incident_state": "6",

#         # INTERNAL resolution code value (NOT label)
#         "close_code": "solved_permanently",

#         # Mandatory notes
#         "close_notes": "Auto-remediation completed. EC2 instance restarted successfully."
#     }

#     r = requests.patch(
#         f"{BASE_URL}/{sys_id}",
#         auth=(SN_USER, SN_PASSWORD),
#         headers={"Content-Type": "application/json"},
#         json=payload
#     )

#     print("🔍 Resolve Status:", r.status_code)
#     print("🔍 Resolve Response:", r.text)

"""
def resolve_incident(sys_id):
   
    payload = {
        "state": "6",               # Resolved
        "incident_state": "6",      # Also set incident_state to satisfy rules
        "close_code": "solved_permanently",  # Resolution code
        "close_notes": "Auto-remediation completed. EC2 instance restarted."  # Close notes
    }

    r = requests.patch(
        f"{BASE_URL}/{sys_id}",
        auth=(SN_USER, SN_PASSWORD),
        headers={"Content-Type": "application/json"},
        json=payload
    )

    print("🔍 Status:", r.status_code)
    print("🔍 Response:", r.text)
    return r

"""


from wsgiref import headers
import requests
from config import SN_INSTANCE, SN_USER, SN_PASSWORD
import http.client
from requests.auth import HTTPBasicAuth

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


# def resolve_incident(sys_id):
#     """
#     Update an existing incident to Resolved state after EC2 restart.
#     Includes all mandatory fields to satisfy data policies.
#     """
#     payload = {
#         "state": "6",               # Resolved
#         "incident_state": "6",      # Also set incident_state
#         "close_code": "solved_permanently",  # Mandatory resolution code
#         "close_notes": "Auto-remediation completed. EC2 instance restarted successfully."  # Mandatory notes
#     }

#     r = requests.patch(
#         f"{BASE_URL}/{sys_id}",
#         auth=(SN_USER, SN_PASSWORD),
#         headers=HEADERS,
#         json=payload
#     )

#     print("🔍 Resolve Status:", r.status_code)
#     print("🔍 Resolve Response:", r.text)
#     return r

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
