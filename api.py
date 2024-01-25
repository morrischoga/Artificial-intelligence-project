import requests
import json
import uuid
analysis_table = "https://api.airtable.com/v0/appSMr3AZADAOcUC4/tblqhearTiTXvECO1"
url = 'https://api.airtable.com/v0/appSMr3AZADAOcUC4/tblqhearTiTXvECO1'
api_key ="patg3nVCYWdoRthJn.56198a4363e0982055386462c75e70566e51bc2b4bac7cd605b6996a87b51521"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

def save_data(args):
    id = uuid.uuid4()
    payload = {
    'records': [
        {
            'fields': {
                'query_id': str(id),
                'client_id': 123,
                'month': args["month"],
                'proba': float(args['proba']),
                'revenue': int(args['revenue'])
            }
        }
    ]
    }
    payload = json.dumps(payload)
    response = requests.post(url, headers=headers, json=json.loads(payload))
    if response.status_code == 200:
        print('API call successful!')
    else:
        print(f'Error: {response.status_code} - {response.text}')


