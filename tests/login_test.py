import requests
json_data = {
    'username': '*****',
    'password': '*****',
}
response = requests.post('https://portal.chiliprotect.com/api/1/login', json=json_data)

print(response.status_code)
authserversecure_cookie = response.cookies.get('AUTH_SERVER_SECURE')
print(authserversecure_cookie)

response = requests.get(
    'https://portal.chiliprotect.com/fc/access',
    cookies=response.cookies,
)
print(response.cookies.get('X-Apigw-Session'))