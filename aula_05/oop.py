# PROGRAMACAO ORIENTADA A OBJETO
# ABSTRACAO == CLASS


# PROFESSORES, ALUNOS => PESSOAS

#ABSTRAÇÃO PESSOA (CLASSE)

class Acoes:
    
    # Methodos
    def nome_em_maiusculo(self):
        return self.nome.upper()

    def nome_em_minusculo(self):
        return self.nome.lower()


class Pessoa:#...

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    # Propriedade nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, v_nome):
        self.__nome = v_nome

    @nome.getter
    def nome(self):
        return self.__verifica_nome(self.__nome)

    #Propriedade email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, v_email):
        self.__email = v_email

    @email.getter
    def email(self):
        return self.__email

    # Methodo privado
    def __verifica_nome(self, nome):
        return nome.strip().capitalize()

# (Pessoal) = mostra a herança adquirida
class Professor(Pessoa, Acoes):
    def __init__(self, nome, email, disciplina):
        super().__init__(nome, email)
        self.disciplina = disciplina

class Aluno(Pessoa, Acoes):
    def __init__(self, nome, email, turma):
        super().__init__(nome, email)
        self.turma = turma

class Disciplina(Acoes):
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

    # @property
    # def materia(self):
    #     return self.__materia

    # @materia.setter
    # def materia(self, v_materia):
    #    self__materia = v_materia

    # @property
    # def carga_horaria(self):
    #     return self.__carga_horaria

    # @carga_horaria.setter
    # def carga_horaria(self, v_carga_horaria):
    #     self.carga_horaria = v_carga_horaria


    

#CLASSE
# print(Pessoa)

#OBJETO
julio = Pessoa('     julio pereira', 'julio@email.com')

# print(julio)

# PROPRIEDADE == ATRIBUTO DA CLASSE 
# print(Pessoa.nome)

#ATRIBUTO == PROPRIEDADE DO OBJETO
# julio.nome = 'julio Pereira'
# julio.email = 'julio@gmail.com'

# print(julio.nome)
# print(julio.email)

# METHODOS
# print(julio.nome_em_maiusculo())

professor = Professor('julio pereira', 'julio@email.com', 'programando em python')

# print(professor.disciplina)

aluno = Aluno('          Pedro', 'pedro@gmail', 't13416')

# print(aluno.nome)
# print(aluno.nome_em_maiusculo())
# print(aluno.nome_em_minusculo())


disciplina = Disciplina('Programando com python', 32)

# print(disciplina.nome)






