import requests

class Config:
    def __init__(self, env):
        # SUPPORTED_ENVS = ['local', 'staging']
        # if env.lower() not in SUPPORTED_ENVS:
        #     raise Exception(F'{env} is not a supported environment (eupported envs: {SUPPORTED_ENVS})')
        self.base_url = {
            'local': 'http://127.0.0.1:5000/login/',
            'staging': 'http://localhost:8000/loginstage/'
        }[env]

class Requests:
    def request(self, url, method='get', **kwargs):
        return requests.request(url=url, method=method, **kwargs)
    
    def get(self, url, **kwargs):
        return self.request(url=url, **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method='post', **kwargs)

    def put(self, url, **kwargs):
        return self.request(url=url, method='put', **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url=url, method='delete', **kwargs)