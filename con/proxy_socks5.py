import requests
import json
import time


class Proxy:
    @staticmethod
    def get():
        while True:
            try:
                req = requests.get(
                    'https://www.proxyscan.io/api/proxy?last_check=3600&type=socks5&limit=10000&ping=100?level=anonymous')
            except:
                time.sleep(3)
                req = requests.get(
                    'https://www.proxyscan.io/api/proxy?last_check=3600&type=socks5&limit=10000&ping=100?level=anonymous')

            if req.status_code == 200:
                data = json.loads(req.content)
                socks_list = []
                for i in data:
                    ip = i['Ip']
                    port = i['Port']
                    socks_list.append(f'socks5://{ip}:{port}')
                return socks_list
