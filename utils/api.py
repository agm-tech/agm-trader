import requests
from utils.logger import logger

url = f'http://api.agmtechnology.com'

def access_api(endpoint, method='GET', data=None):
    try:
        
        # Add timeout to prevent hanging
        auth = requests.post(
            url + '/login', 
            json={'username': 'admin', 'password': 'password'},
        )
        
        response = requests.request(
            method, 
            url + endpoint, 
            json=data, 
            headers={'Authorization': f'Bearer {auth.json()["access_token"]}'},
        )
        
        try:
            return response.json()
        except:
            return response.content
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        raise