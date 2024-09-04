import requests
import re
from stem import Signal
from stem.control import Controller


def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    return session


def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="parrot")
        controller.signal(Signal.NEWNYM)


def createOnionList(fileName, regex):
    onionListFile = open(fileName, "r").read()
    return re.findall(regex, onionListFile, re.MULTILINE)


def identifyRegex(regex, text):
    return re.findall(regex, text, re.IGNORECASE | re.MULTILINE)



#MULTILINE separa cada match em uma posicao
#IGNORECASE nao deixa sensivel a letras minusculas ou maiusculas

fileName = "onionList.txt"
regexOnion = r".*\.onion.*$"
onionListList = createOnionList(fileName, regexOnion)

regexes = {
    'Bitcoin': r'\b3[a-zA-Z0-9]{24,}\b|\b1[a-zA-Z0-9]{24,36}\b|\bbc1[a-zA-Z0-9]{22,}',
    'Ethereum': r"\b0x[a-zA-Z0-9]{23,}\b",
    'Tron': r'\bT[a-zA-Z0-9]{24,}\b',
    'BNB': r'\bbnb[a-zA-Z0-9]{22,}\b',
    'XRP': r'\br[a-zA-Z0-9]{24,}\b',
    'Cardano': r'\baddr[a-zA-Z0-9]{24,}\b',
    "Polkadot": r'\b1[a-zA-Z0-9]{37,}\b',
    "Dogecoin": r'\bD[a-zA-Z0-9]{25,}\b',
    "Monero": r'\b4[a-zA-Z0-9]{94}\b|\b8[a-zA-Z0-9]{94}\b'
}

cont = 0

'''for onion in onionListList:
    print(f"\nAcessando o site {cont}: http://{onion}\n")
    cont = cont + 1'''

file = open("carteiras.txt", "w")

for onion in onionListList:
    try:
        print(f"\nAcessando o site: http://{onion}\n")

        renew_connection()
        session = get_tor_session()
        print(f'Refazendo conexao: , {session.get("http://httpbin.org/ip").text}\n')

        r = session.get('http://'+onion)

        for wallet, regex in regexes.items():
            regexSiteList = identifyRegex(regex, r.text)
            print(f"Matches: {regexSiteList}\n")
            print(f"______________________________________________________________________________________________________")
            file.write(f"Carteiras: {regexSiteList}, Tipo de carteira : {wallet}, Site: http://{onion}\n")

    except:
        print(f"______________________________________________________________________________________________________\n")
        print("Deu erro, proximo site...\n")
        print(f"______________________________________________________________________________________________________\n")