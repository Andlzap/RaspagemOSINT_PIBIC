import requests
from stem import Signal
from stem.control import Controller


class TorUtils:
    def __init__(self, tor_host="127.0.0.1", tor_port=9050, control_port=9051, password="parrot"):
        self.tor_host = tor_host
        self.tor_port = tor_port
        self.control_port = control_port
        self.password = password
    
    def get_tor_session(self):
        session = requests.session()
        session.proxies = {'http': f'socks5h://{self.tor_host}:{self.tor_port}',
                           'https': f'socks5h://{self.tor_host}:{self.tor_port}'}
        return session
    
    def renew_connection(self):
        with Controller.from_port(port=self.control_port) as controller:
            controller.authenticate(password=self.password)
            controller.signal(Signal.NEWNYM)
