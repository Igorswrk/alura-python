import re

class ExtractURL:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        template = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = template.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_base_url(self):
        index_query = self.url.find('?')
        base_url = self.url[:index_query]
        return base_url

    def get_parameters_url(self):
        index_query = self.url.find('?')
        parameters_url = self.url[index_query + 1:]
        return parameters_url

    def get_parameters_value(self, search_parameter):
        index_parameter = self.get_parameters_url().find(search_parameter)
        index_value = index_parameter + len(search_parameter) + 1
        index_ampersand = self.get_parameters_url().find('&', index_value)
        if index_ampersand == -1:
            value = self.get_parameters_url()[index_value:]
        else:
            value = self.get_parameters_url()[index_value:index_ampersand]
        return value


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extractor_url = ExtractURL(url)
value_qtd = extractor_url.get_parameters_value("quantidade")
print(value_qtd)
