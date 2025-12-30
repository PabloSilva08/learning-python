def conjunto_de_questoes() -> list[dict]:
    ques = [
        {
            'Pergunta': 'Quanto é 2 + 2?',
            'Opcoes': {'a)': '1', 'b)': '3', 'c)': '4', 'd)': '5',},
            'Resposta': 'c',
        },
        {
            'Pergunta': 'Quanto é 5 x 5?',
            'Opcoes': {'a)': '55', 'b)': '25', 'c)': '10', 'd)': '51',},
            'Resposta': 'b',
        },
        {
            'Pergunta': 'Quanto é 10 / 2?',
            'Opcoes': {'a)': '5', 'b)': '4', 'c)': '2', 'd)': '1',},
            'Resposta': 'a',
        },
        {
            'Pergunta': 'Quanto é 2 x 2?',
            'Opcoes': {'a)': '0', 'b)': '1', 'c)': '2', 'd)': '4',},
            'Resposta': 'd',
        },
    ]
    return(ques)

def lancar_pergunta(questao: list[dict]) -> str:
    print(questao.get('Pergunta'))
    for op, resp in questao.get('Opcoes').items():
        print(op, resp)
    return(questao.get('Resposta'))

def compare_answer(correct_answer, supposed_answer) -> int:
    if (correct_answer == supposed_answer):
        print("Acertou...")
        return(1)
    else:
        print("Errou...")
        return(0)

if "__main__" == __name__:
    count: int = 0
    questoes = conjunto_de_questoes()

    for questao in questoes:
        responder = input('Digite "S" para sair ou qualquer outra para responder: ').lower()
        if( responder != 's' ):
            correct_answer: str = lancar_pergunta(questao)
            supposed_answer: str = input('Escreva a opcao correta: ').lower()
            count += compare_answer(correct_answer, supposed_answer)
            print('#' * 80)
        else:
            break
    print("Você obteve,", count, "acerto(s).")
