class Configuration:

    def __init__(self, host: str, username: str, password: str, proxies=None):
        self.host = host
        self.username = username
        self.password = password
        self.proxies = proxies if proxies else {}
