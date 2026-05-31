import colorama

# Inicializa o colorama para garantir compatibilidade no terminal
colorama.init()

# 1. Lista para armazenar as mensagens e cores do reservatório
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": colorama.Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": colorama.Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": colorama.Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": colorama.Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": colorama.Fore.BLUE}
]

# 2. Função responsável por definir a cor conforme o nível informado
def verificar_nivel(nivel_informado):
    for item in niveis_agua:
        if item["nivel"] == nivel_informado:
            # 3. Exibir no terminal a situação atual com a cor correspondente
            print(f"Nível {item['nivel']}: {item['cor']}{item['situacao']}")
            # 4. Restaurar o estilo padrão do terminal
            print(colorama.Style.RESET_ALL, end="")
            return
    print("Nível inválido!")

# --- Simulação do Sistema ---
print("--- SIMULAÇÃO DE MONITORAMENTO DO RESERVATÓRIO ---")
verificar_nivel(1)
verificar_nivel(2)
verificar_nivel(3)
verificar_nivel(4)
verificar_nivel(5)