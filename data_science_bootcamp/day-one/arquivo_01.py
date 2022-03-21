# Aula 01 Automatização 
# Criar um código que automatize a analise de uma tabela e envie os resultados por email

import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.hotkey('win', 's')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3
)
pyautogui.click(1062, 622)
link = 'https://drive.google.com/drive/mobile/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym?usp=sharing'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(15)
pyautogui.click(1021, 350)
pyautogui.click(1071, 170)
pyautogui.click(972, 556)
time.sleep(8)
table = pd.read_excel(r'C:\Users\Marcelo Simas\Downloads\Vendas - Dez.xlsx')
faturamento = table['Valor Final'].sum()
qtd_produtos = table['Quantidade'].sum()
pyautogui.hotkey('ctrl', 't')
link = 'mail.google.com'
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(76, 172)
time.sleep(2)
pyautogui.write('rubskaiserman312@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Relatório')
pyautogui.press('tab')
pyautogui.write(f'''Presados, Segue abaixo o relatório do dia.

Faturamento: R${faturamento:.2f}
Quantidade de produtos: {qtd_produtos}

abs, Rubens''')
pyautogui.hotkey('ctrl', 'enter')
