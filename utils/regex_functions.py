import re

class RegexUtils:
    def __init__(self):
        pass
    
    def create_onion_list(self, file_name, regex):
        with open(file_name, "r") as onion_file:
            onion_list = onion_file.read()
        return re.findall(regex, onion_list, re.MULTILINE)
    
    def identify_regex(self, regex, text):
        return re.findall(regex, text, re.IGNORECASE | re.MULTILINE)


#MULTILINE separa cada match em uma posição
#IGNORECASE não deixa sensível a letras minúsculas e maiúsculas