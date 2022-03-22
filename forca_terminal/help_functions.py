import os

def get_answer() -> list:
    ans = list(input('Insira a palavra de resposta: ').lower())
    os.system('cls' if os.name == 'nt' else 'clear')
    return ans

def get_chute(palpites: list, opcoes: list , repeticao=False) -> list:
    if repeticao:
        print('Termo inserido não incluso nas opções')
    print(f"\nOpções: {' '.join(opcoes)}")
    print(f'\nPalpites Dados: {" ".join(palpites)}')
    chute = input('\nInsira seu palpite: ').lower()
    if chute not in palpites and chute in opcoes:
        palpites.append(chute)
        opcoes.remove(chute)
        return [palpites, opcoes]
    else:
        return get_chute(palpites, opcoes, True)

def check_endgame(palpites: list, ans: list) -> bool:
    for letter in ans:
        if letter not in palpites:
            return False

    return True

def build_forca(ans: list, life: int, palpites: list) -> None:
    print(" ___")
    print(" |  |")
    print(" |  O") if life < 6 else print(" |  ")
    if life == 4:
        print(" |  |")
    elif life == 3:
        print(" | /|")
    elif life < 3:
        print(" | /|\\")
    else: 
        print(" |  ")
    if life == 1:
        print(" |  /")
    elif life == 0:
        print(" |  /\\")
    else:
        print(" |")    
    print('_|_', end='           ')

    for letter in ans:
        print(letter, end=' ') if letter in palpites else print('_', end=' ')
    print()
