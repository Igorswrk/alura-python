file = open('dados/contacts_write.csv', encoding='latin_1', mode='a+')

print(type(file.buffer))

texto_em_bytes = bytes('Esse é um texto em bytes', 'latin_1')
# print(texto_em_bytes)
# print(type(texto_em_bytes))

contact = bytes('15,Verônica,veronica@veronica.com.br\n', 'latin_1')
file.buffer.write(contact)

file.close()