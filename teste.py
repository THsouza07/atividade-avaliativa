class Aluno():
    def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

aluno1=Aluno(1234, 'Thiago', 'masculino', 17) 
print('matricula', aluno1.matricula)
print('nome', aluno1.nome)
print('sexo', aluno1.sexo)
print('idade', aluno1.idade)       