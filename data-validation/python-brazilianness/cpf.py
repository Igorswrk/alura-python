from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!")

    def cpf_is_valid(self, document):
        if len(document) == 11:
            validator = CPF()
            return validator.validate(document)
        else:
            raise ValueError("Quantidade de digitos invalida!")

    def format_cpf(self):
        mask_ = CPF()
        return mask_.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()