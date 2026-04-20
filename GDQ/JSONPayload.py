import requests

url = 'http://localhost:8000/api/GDQPortal/'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYyNDk0NTQ2LCJpYXQiOjE3NjI0OTA5NDYsImp0aSI6ImI0MTZmZjgyZjMzNzQxNTNiOGRmMWFhMzVkODQ0N2NhIiwidXNlcl9pZCI6IjEifQ.XmZuJonKW0Dxbl8gHCHuA-FaWaqKkZuadaRfpps_zlM'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

data = {
    "process_number": "PRC002",
    "process_name": "Improve Outage Reporting",
    "process_issue": "Delayed outage notifications",
    "process_solution": "Integrate real-time alerts",
    "process_benefits": "Faster response, improved customer satisfaction",
    "process_start_date": "2025-11-06",
    "process_completion_date": "2025-12-10",
    "process_status": "inprogress"
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())