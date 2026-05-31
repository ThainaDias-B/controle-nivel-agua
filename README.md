# controle-nivel-agua
# 🚰 Sistema de Monitoramento de Níveis de Água

Este projeto foi desenvolvido como uma atividade prática para a disciplina de **Desenvolvimento de Sistemas I (Agenda 11 - Bibliotecas)**. 

O objetivo do sistema é simular o monitoramento do terminal de um reservatório de água, exibindo mensagens de alerta customizadas com cores diferentes de acordo com o nível de criticidade atual do reservatório.

## 🚀 Funcionalidades

O programa foi estruturado seguindo os requisitos solicitados:
* **Estrutura de dados:** Utilização de listas e dicionários para mapear e organizar os níveis, situações de risco e suas respectivas cores.
* **Modularização:** Criação de funções dedicadas para realizar a busca e validação do nível informado, mantendo o código limpo e legível.
* **Interface Visual de Console:** Integração com a biblioteca externa `colorama` para estilizar o terminal.
* **Reset de Estilo:** Aplicação de boas práticas de programação limpando a formatação do terminal ao final da execução (`Style.RESET_ALL`), evitando efeitos colaterais em mensagens posteriores.

## 🎨 Tabela de Níveis e Cores Utilizadas

| Nível | Situação | Cor no Terminal |
| :---: | :--- | :--- |
| Nível 1 | Muito baixo (crítico) | Vermelho 🔴 |
| Nível 2 | Baixo | Amarelo 🟡 |
| Nível 3 | Médio | Verde 🟢 |
| Nível 4 | Alto | Ciano 🔵 |
| Nível 5 | Muito alto (alerta) | Azul 🔵 |

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Colorama** (Biblioteca externa para controle de cores no terminal)
