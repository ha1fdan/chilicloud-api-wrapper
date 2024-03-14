import requests

cookies = {
    'device_cookie': '',
    'rest_access_token': '',
    'server_return_to': '',
    '_activecho_session': '',
    'dc_id': '',
    'host': 'https://portal.chiliprotect.com',
    'accountsrv_locale': 'da',
}

response = requests.get('https://portal.chiliprotect.com/fc/access', cookies=cookies)
print(response.cookies)