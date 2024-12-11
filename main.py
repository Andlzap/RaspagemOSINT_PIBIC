from utils.tor_functions import TorUtils
from utils.regex_functions import RegexUtils
from utils.text_analysis_functions import TextAnalysis
from dictionaries.criptos import criptosDictionary
from dictionaries.crimes import crimesDictionary

#Classes
tor_utils = TorUtils()
regex_utils = RegexUtils()
text_analysis = TextAnalysis(crimesDictionary)

fileName = "onionList.txt"
regexOnion = r".*\.onion.*$"
onionListList = regex_utils.create_onion_list(fileName, regexOnion)

file = open("wallets.txt", "w")

for onion in onionListList:
    try:
        print(f"\nAccessing the website: http://{onion}\n")

        tor_utils.renew_connection()
        session = tor_utils.get_tor_session()
        print(f'Reconnecting: , {session.get("http://httpbin.org/ip").text}\n')

        r = session.get('http://' + onion)
        
        # Identificando carteiras
        for wallet, cripto in criptosDictionary.items():
            regexSiteList = regex_utils.identify_regex(cripto, r.text)
            print(f"Matches: {regexSiteList}\n")
            print(f"______________________________________________________________________________________________________")
            file.write(f"Wallets: {regexSiteList}, Wallet type: {wallet}, Site: http://{onion}\n")

        analysis = text_analysis.analyze(r.text)
        print(f"Crimes detected: {analysis}")
        file.write(f"Crimes detected: {analysis}")
        file.write(f"\n\n")

    except Exception as e:
        print(f"______________________________________________________________________________________________________\n")
        print(f"Error, next site... Error: {e}\n")
        print(f"______________________________________________________________________________________________________\n")
