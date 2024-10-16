# Sistema de Inferência Fuzzy para Cálculo de Gorjeta em Restaurante

Este projeto implementa um sistema de inferência fuzzy em Python para calcular o percentual de gorjeta sugerido em um restaurante, baseado em três variáveis: qualidade da refeição, serviço e tempo de atendimento. A partir dessas variáveis, o sistema utiliza regras fuzzy para determinar o valor adequado de gorjeta.

## Descrição do Problema

O cálculo da gorjeta leva em consideração as seguintes regras:

1. Se a refeição estiver insossa e o serviço ruim, a gorjeta será pouca.
2. Se a refeição estiver saborosa e o serviço excelente, a gorjeta será generosa.
3. Se o tempo de atendimento for demorado, não haverá gorjeta.
4. Se o tempo de atendimento for mediano ou rápido, haverá gorjeta, dependendo da qualidade da refeição e do serviço.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **NumPy**: Biblioteca para suporte a arrays e funções matemáticas.
- **scikit-fuzzy**: Biblioteca para implementação de lógica fuzzy.
  
## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/fuzzy-tip-calculator.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd fuzzy-tip-calculator
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar

Após clonar o repositório e instalar as dependências, você pode executar o script para calcular o percentual de gorjeta sugerido. Certifique-se de ter o **Python** instalado.

1. Edite as variáveis de entrada para a qualidade da refeição, serviço e tempo de atendimento no arquivo principal:
    ```python
    tipping.input['quality'] = 7  # Qualidade da refeição (0 a 10)
    tipping.input['service'] = 9.8  # Qualidade do serviço (0 a 10)
    tipping.input['wait_time'] = 20  # Tempo de atendimento em minutos (0 a 60)
    ```

2. Execute o script:
    ```bash
    python fuzzy_tip_calculator.py
    ```

ref -> https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_tipping_problem_newapi.html
