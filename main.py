import requests

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-Modified-Since': 'Sun, 14 Jul 2024 03:46:33 GMT',
    'Priority': 'u=1, i',
    'Referer': 'https://www.mut.gg/players/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://www.mut.gg/api/mutdb/prices/overall/playeritem/?external_ids=57217537%2C57222072%2C57202575%2C57222691%2C57203056%2C57203058%2C71020948%2C71031543%2C71022534%2C71031523%2C44016587%2C44027730%2C44000796', headers=headers)

print(response.status_code)
print(response.request.headers)
