# Projeto de análise de dados de entradas e saídas
Este projeto inclui um script em Python que utiliza a biblioteca Pandas e Plotly para ler um arquivo csv e criar gráficos de barra para análise de informações e números. 
O objetivo é analisar dados de entradas e saídas de produtos da mercearia, visualizar total de gastos e ganhos, e avaliar quais produtos são mais ou menos vendidos.

## Script

O script realiza o seguinte:

1. **Carrega e processa dados:** Carrega dados de vendas e compras a partir de um arquivo csv informado previamente.
2. **Calcula valores totais:** Calcula o valor total gasto e ganho com base na quantidade e preço dos produtos.
3. **Cria gráficos:** Gera gráficos de barras que mostram:
   - Total de gastos por compra de produto.
   - Total de ganhos por venda de produto.
   - Comparação entre os dois dados acima.
   - Análise de produtos mais e menos vendidos com valores formatados dentro das barras.

## Requisitos

- Python 3.12
- Bibliotecas python:
  - `pandas`
  - `plotly`

Instalar as dependências:

```bash
pip install pandas plotly
