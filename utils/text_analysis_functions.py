class TextAnalysis:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    
    def analyze(self, text: str) -> set:
        result = set()
        words = set(text.upper().split())
        
        for key, list_value in self.dictionary.items():
            for value in list_value:
                if any(value.upper() in word for word in words):
                    result.add(key)
        
        if not result:
            return None
        return result


#text.upper(): transforma o texto em letras maiúsculas, para garantir que a busca seja insensível a maiúsculas/minúsculas.
#.split(): divide o texto em uma lista de palavras com base nos espaços em branco.
#set(): converte a lista de palavras em um conjunto, para que cada palavra seja única (sem repetições).