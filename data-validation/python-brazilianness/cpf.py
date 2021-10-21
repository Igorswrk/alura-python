class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_is_valid(self, document):
        if len(document) == 11:
            return True
        else:
            return False

    def format_cpf(self):
        frist_slice = self.cpf[:3]
        second_slice = self.cpf[3:6]
        third_slice = self.cpf[6:9]
        fourth_slce = self.cpf[9:]

        return f'{frist_slice}.{second_slice}.{third_slice}-{fourth_slce}'
