class Config:
    def __init__(self, env):
        # SUPPORTED_ENVS = ['local', 'staging']
        # if env.lower() not in SUPPORTED_ENVS:
        #     raise Exception(F'{env} is not a supported environment (eupported envs: {SUPPORTED_ENVS})')
        self.base_url = {
            'local': 'http://127.0.0.1:5000/login/',
            'staging': 'http://localhost:8000/loginstage/'
        }[env]
