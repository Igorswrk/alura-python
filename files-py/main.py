contacts_file = open('font_files/contacts.csv', encoding='latin_1')

"""
contacts_file.readlines() -> ler todas as linhas do arquivo
contacts_file.readline() -> ler 1 linha por vez do arquivo

"""

for line in contacts_file: # Nao gasta muita memória pois não salva o arquivo todo
    print(line, end='')