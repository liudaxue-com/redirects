import json
import re

def lambda_handler(event, context):
    with open('./redirects_active.json', 'r') as f:
        data = json.loads(f.read())
        name = re.search(r'(.*)\.流大学\.com', event['headers']['host'].encode('utf-8').decode('idna'))[1]
        if name not in data:
            location = 'https://xn--tiq.xn--pss25c012a.com/not_found.html'
        else:
            location = data[name]
        return {
            'statusCode': 302,
            'headers': {
                'Location': location
            },
            'body': f'Redirecting to <a href="{location}">{location}</a>'
        }
