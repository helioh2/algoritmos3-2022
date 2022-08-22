class Pessoa:

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    
    def __hash__(self) -> int:
        return hash(self.cpf)

    def __str__(self) -> str:
        return str(self.__dict__)


pessoa1 = Pessoa("Joao", "27272727", "joao@uol.com")
pessoa1.nome = "Joao das Neves"   # OBJETO MUTÁVEL


nome = "Maria"
nome = nome + "das Neves"  # não está alterando o objeto- (string) 'nome', está criando uma nova string

