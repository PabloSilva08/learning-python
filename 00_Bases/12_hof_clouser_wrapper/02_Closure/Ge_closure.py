print("Exercício 01")
print()

from typing import Callable

def fazer_lembrete(mensagem: str) -> Callable[[], None]:
    def imprimir_mensagem() -> None:
        print(mensagem)

    return imprimir_mensagem


lembrar_cafe = fazer_lembrete("Beber café!")
lembrar_cafe() # Deve imprimir: Beber café!

###############################################################################
print()
print("=" * 60)
print("Exercício 02")
print()

from typing import Callable

def gerar_formatador(prefixo: str) -> Callable[[str], str]:
    def gerar_texto(texto: str) -> str:
        return f"{prefixo}: {texto}"

    return gerar_texto

formatar_erro = gerar_formatador("ERRO")
formatar_log = gerar_formatador("LOG")

print(formatar_erro("Arquivo não encontrado")) # "ERRO: Arquivo não encontrado"
print(formatar_log("Usuário logado"))          # "LOG: Usuário logado"

###############################################################################
print()
print("=" * 60)
print("Exercício 03")
print()

from typing import Callable

def fabricar_calculadora_imposto(taxa: float) -> Callable[[float], float]:
    def calcular_taxa(valor_produto: float) -> float:
        return taxa * valor_produto

    return calcular_taxa

imposto_iss = fabricar_calculadora_imposto(0.05) # 5%
imposto_icms = fabricar_calculadora_imposto(0.18) # 18%

print(imposto_iss(100.0))  # Deve imprimir 5.0
print(imposto_icms(100.0)) # Deve imprimir 18.0

###############################################################################
print()
print("=" * 60)
print("Exercício 04")
print()

from typing import Callable

def criar_gerador_id(inicio: int) -> Callable[[], int]:
    def numero_id() -> int:
        nonlocal inicio
        inicio += 1
        return inicio

    return numero_id

gerar_pedido_id = criar_gerador_id(100)

print(gerar_pedido_id()) # 101
print(gerar_pedido_id()) # 102
print(gerar_pedido_id()) # 103

###############################################################################
print()
print("=" * 60)
print("Exercício 05")
print()

from typing import Callable

def criar_calculadora_media() -> Callable[[float], float]:
    numero: float = 0.0
    quantidade: int = 0
    def media_aritmetica(novo_valor: float) -> float:
        nonlocal numero
        nonlocal quantidade
        numero += novo_valor 
        quantidade += 1
        return numero / quantidade
    
    return media_aritmetica

media = criar_calculadora_media()

print(media(10)) # Retorna 10.0 (10 / 1)
print(media(20)) # Retorna 15.0 ( (10 + 20) / 2 )
print(media(30)) # Retorna 20.0 ( (10 + 20 + 30) / 3 )

###############################################################################
print()
print("=" * 60)
print("Exercício 06")
print()

from typing import Callable

def configurar_validador(senha_correta: str, tentativas_maximas: int) -> Callable[[str], str]:
    def senha_tentada(tentativa: str) -> str:
        nonlocal tentativas_maximas

        if tentativas_maximas < 1:
            return "Acesso bloqueado"
        if senha_correta == tentativa:
            return "Acesso permitido"
        tentativas_maximas -= 1
        if tentativas_maximas <= 0:
            return "Acesso bloqueado"
        return f"Senha incorreta. Tentativas restantes: {tentativas_maximas}"

    return senha_tentada


validar = configurar_validador("1234", 2)

print(validar("0000")) # "Senha incorreta. Tentativas restantes: 1"
print(validar("1111")) # "Acesso bloqueado"
print(validar("1234")) # "Acesso bloqueado" (mesmo com a senha certa, pois estouro

###############################################################################
print()
print("=" * 60)
print("Exercício 07")
print()

from typing import Callable

def criar_cache() -> Callable[[int], str]:
    historico = {}
    def o_dobro(n: int) -> str:
        if historico.get(n, False) != False:
            return f"Retornando do cache: {historico[n]}"
        historico[n] = n * 2
        return f"Calculado agora: {historico[n]}"

    return o_dobro

cache = criar_cache()

###############################################################################
###############################################################################
#correcao minima
#
#print(cache(5)) # "Calculado agora: 10"
#print(cache(5)) # "Retornando do cache: 10"
#print(cache(10)) # "Calculado agora: 20"
#
#def criar_cache() -> Callable[[int], str]:
#    historico = {}
#    def o_dobro(n: int) -> str:
#        # Forma mais segura e legível de checar chaves
#        if n in historico:
#            return f"Retornando do cache: {historico[n]}"
#        
#        resultado = n * 2
#        historico[n] = resultado
#        return f"Calculado agora: {resultado}"
#
#    return o_dobro
###############################################################################
###############################################################################
# Pythonico
#
#def criar_cache() -> Callable[[int], str]:
#    historico = {}
#    def o_dobro(n: int) -> str:
#        valor = historico.get(n)
#        if valor is not None: # Verifica se a chave existia
#            return f"Retornando do cache: {valor}"
#        
#        resultado = n * 2
#        historico[n] = resultado
#        return f"Calculado agora: {resultado}"
#    return o_dobro

###############################################################################
###############################################################################
###############################################################################

print()
print("=" * 60)
print("Exercício 08")
print()

from typing import Callable

def criar_conta_bancaria(saldo_inicial: float) -> Callable[[str, float], str]:
    saldo: float = saldo_inicial
    def movimentacao_financeira(operacao: str, valor: float) -> str:
        nonlocal saldo
        if operacao == "depositar":
            saldo = saldo + valor
            return f"Saldo: {saldo}"
        if operacao == "sacar":
            if saldo < valor:
                return "Saldo insuficiente"
            saldo = saldo - valor
            return f"Saldo: {saldo}"
        if operacao == "consultar":
            return f"Saldo: {saldo}"
        return "Operacao invalida."

    return movimentacao_financeira




conta = criar_conta_bancaria(100.0)

print(conta("depositar", 50)) # 150.0
print(conta("sacar", 200))    # "Saldo insuficiente"
print(conta("sacar", 30))     # 120.0
print(conta("consultar", 0))  # 120.0

###############################################################################
###############################################################################
###############################################################################
#from typing import Callable, Any
#
#def criar_conta_bancaria(saldo_inicial: float) -> Callable[[str, float], Any]:
#    saldo = saldo_inicial
#
#    def depositar(v: float):
#        nonlocal saldo
#        saldo += v
#        return saldo
#
#    def sacar(v: float):
#        nonlocal saldo
#        if v > saldo: return "Saldo insuficiente"
#        saldo -= v
#        return saldo
#
#    def consultar(_: float): # Ignora o valor
#        return saldo
#
#    acoes = {"depositar": depositar, "sacar": sacar, "consultar": consultar}
#
#    def movimentacao(operacao: str, valor: float) -> Any:
#        if operacao in acoes:
#            return acoes[operacao](valor)
#        return "Operação inválida"
#
#    return movimentacao
