from create_docs import Document

from phones import PhonesBr
from validate_docbr import CPF
from validate_docbr import CNPJ

cnpj = CNPJ()
cpf = CPF()

# cpf_user = Cpf("09962725690")
# print(cpf_user)

new_cpnj = cnpj.generate()
new_cpf = cpf.generate()

document = Document.create_new(new_cpnj)
print(document)

phone = "552126481234"
new_phone = PhonesBr(phone)

print(new_phone)