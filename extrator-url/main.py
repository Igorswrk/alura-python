url = "bytebank.com/cambio?moedaOrigem=real"  # Strings no Python são objetos imutáveis!
print(url)


url_base = url[0:19]
print(url_base)

url_parameters = url[20:36]
print(url_parameters)

"""
URLs e seus formatos: como as URLs funcionam e o que cada parte de uma URL significa - base e parâmetros.

O operador de fatiamento [a:b], utilizado para obter uma substring desde o índice a até o índice b - 1 da string 
original. Lembrando que b - 1 pois o segundo argumento do fatiamento é exclusivo.

A string original não é alterada ao ser fatiada devido à sua imutabilidade.
"""