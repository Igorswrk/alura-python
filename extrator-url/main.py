url = "bytebank.com/cambio?moedaOrigem=real"  # Strings no Python são objetos imutáveis!
print(url)


url_base = url[0:19]
print(url_base)

url_parameters = url[20:36]
print(url_parameters)
