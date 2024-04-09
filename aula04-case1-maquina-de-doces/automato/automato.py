import time
import os

alfabeto = {
    0: 0, 
    1: 1, 
    2: 2, 
    3: 3, 
    5: 4
}
estado_inicial = "0"
estados_finais = ("d1", "d2", "d3")
transicoes = {
    "0": [None, 1, 2, None, 5],
    "1": [None, 2, 3, None, 6],
    "2": [None, 3, 4, None, 7],
    "3": [None, 4, 5, None, "p3"],
    "4": [None, 5, 6, None, "p3"],
    "5": [None, 6, 7, None, "p3"],
    "6": ["p1", 7, "p3", None, "p3"],
    "7": ["p2", "p3", "p3", None, "p3"],
    "p1": [6, "d1", None, None, None],
    "p2": [7, "d1", "d2", None, None],
    "p3": [None, "d1", "d2", "d3", None],
    "d1": [None, None, None, None, None],
    "d2": [None, None, None, None, None],
    "d3": [None, None, None, None, None]
}
doces = [
    "1 -- bombom: R$6,00",
    "2 -- kitkat: R$ 7,00",
    "3 -- snickers: R$ 8,00"
]


exemplos_cadeias = [
    [2, 2, 2, 0, 1],
    [5, 5, 3],
    [5, 2, 1, 3],
    [5, 1, 0, 2], # ERRO
    [1, 1, 1, 1, 1, 1, 0, 1]
]
estado_atual = estado_inicial
valor_adicionado = 0
print(f"Estado inicial: {estado_atual}")
for entrada in exemplos_cadeias[0]:
    time.sleep(5)
    os.system("cls")
    if estado_atual.isnumeric() or valor_adicionado < 6:
        if entrada: print(f"Adicionando R${entrada:.2f}")
        valor_adicionado += entrada
    elif estado_atual[0] == "p":
        print(f"Escolhendo entre os doces: {list(range(1, int(estado_atual[-1])+1))}")

    estado_atual = str(transicoes[estado_atual][alfabeto[entrada]])
    if estado_atual == "None":
        print("String inválida!!")
        break
    print(f"ENTRADA: {entrada}, ESTADO: {estado_atual}")

    if estado_atual == "d1":
        print(f"Bom Bom liberado, troco: R${valor_adicionado - 6:.2f}")
    elif estado_atual == "d2":
        print(f"KitKat liberado, troco: R${valor_adicionado - 7:.2f}")
    elif estado_atual == "d3":
        print(f"Snickers liberado, troco: R${valor_adicionado - 8:.2f}")
if (estado_atual[0] != "d") & (estado_atual != "None"):
    print("String inválida")
    

