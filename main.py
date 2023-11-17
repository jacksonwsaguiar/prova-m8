import re
terminal = ""

intencoes = {
    ".*\\batualizar\\b.*|.*\\bpagamento\\b.*|.*\\bmudar\\b.*":"atualizar pagamento",
    ".*\\bstatus\\b.*|.*\\bentrega\\b.*|.*\\brastrear\\b.*|.*\\bonde\\b.*": "acompanhar pedido"
};
acoes ={
    "atualizar pagamento":"prosseguindo para atualizar o metodo de pagamento...",
    "acompanhar pedido":"buscando informações sobre o pedido..."
};

def output(inputStr):
    for key, intention in intencoes.items():
        pattern = re.compile(key)
        ac = pattern.findall(inputStr)
        if ac:
            print("OK")
            print(acoes[intention])
            break
        else:
            print("nada relacionado")

while terminal.lower() !="sair":
    terminal = input('O que deseja fazer?')
    output(terminal)
   
    
    
    
    
