try:
   with open('font_files/contacts.csv', encoding='latin_1') as contacts_file:
        for line in contacts_file: # Nao gasta muita memória pois não salva o arquivo todo
            print(line, end='')
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("no write permission")

"""
contacts_file.readlines() -> ler todas as linhas do arquivo
contacts_file.readline() -> ler 1 linha por vez do arquivo

"""