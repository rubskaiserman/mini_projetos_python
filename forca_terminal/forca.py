from string import ascii_lowercase as alfa
import help_functions as fn

def main():
    input('Garanta que ninguém está vendo e aperte enter para inserir a palavra resposta... ')
    ans = fn.get_answer()
    opcoes, palpites, life = list(alfa), [], 6
    while True:
        fn.build_forca(ans, life, palpites)
        if life == 0:
            print('Derrota...')
            print(f'A resposta era: {"".join(ans)}')
            break
        
        if fn.check_endgame(palpites, ans):
            print("VITÓRIA!!!!")  
            break
        res = fn.get_chute(palpites, opcoes)
        palpites, opcoes = res[0], res[1]
        life -= 1 if palpites[-1] not in ans else 0

if __name__ == "__main__":
    main()



