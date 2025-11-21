class Pessoa:
    populacao = 0
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1
    
    @classmethod
    def total_pessoas(cls):
        return f"Total: {cls.populacao}"

pessoa1 = Pessoa("Maria")
pessoa2 = Pessoa("João")

# Funciona pela classe
print(Pessoa.total_pessoas())  # Total: 2

# Também funciona pela instância
print(pessoa1.total_pessoas())  # Total: 2

print('-' * 80)
pessoa3 = Pessoa("Pablo")
print(Pessoa.total_pessoas())  
print(pessoa1.total_pessoas())  
print(pessoa2.total_pessoas())  
print(pessoa3.total_pessoas())  


print('-' * 80)
print(id(Pessoa.total_pessoas))  
print(id(pessoa1.total_pessoas))  
print(id(pessoa2.total_pessoas))  
print(id(pessoa3.total_pessoas))  

print('-' * 80)
pessoa4 = Pessoa("Capitao America")
print(Pessoa.total_pessoas())  
print(pessoa1.total_pessoas())  
print(pessoa2.total_pessoas())  
print(pessoa3.total_pessoas())  
print(pessoa4.total_pessoas())  

print('-' * 80)
pessoa5 = Pessoa("Vasco")
print(Pessoa.total_pessoas())  
print(pessoa1.total_pessoas())  
print(pessoa2.total_pessoas())  
print(pessoa3.total_pessoas())  
print(pessoa4.total_pessoas())  
print(pessoa5.total_pessoas())  


print('-' * 80)
print(id(Pessoa.total_pessoas))  
print(id(pessoa1.total_pessoas))  
print(id(pessoa2.total_pessoas))  
print(id(pessoa3.total_pessoas))  
print(id(pessoa4.total_pessoas))  
print(id(pessoa5.total_pessoas))  
