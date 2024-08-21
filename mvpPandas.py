import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

dados_entradas = pd.read_csv('entradass.csv')
dados_saidas = pd.read_csv('saidass.csv')

dados_entradas['valorTotal'] = dados_entradas['qtdProduto'] * dados_entradas['valorMovimentacao']
dados_saidas['valorTotal'] = dados_saidas['qtdProduto'] * dados_saidas['valorMovimentacao']

dados_agrupados_entradas = dados_entradas.groupby('nomeProduto').agg({'valorTotal': 'sum'}).reset_index()
dados_agrupados_entradas = dados_agrupados_entradas.sort_values(by='valorTotal', ascending=False)
dados_agrupados_saidas = dados_saidas.groupby('nomeProduto').agg({'valorTotal': 'sum'}).reset_index()
dados_agrupados_saidas = dados_agrupados_saidas.sort_values(by='valorTotal', ascending=False)

dados_agrupados_entradas['valorTotalFormatado'] = dados_agrupados_entradas['valorTotal'].apply(lambda x: f'R$ {x:.2f}')
dados_agrupados_saidas['valorTotalFormatado'] = dados_agrupados_saidas['valorTotal'].apply(lambda x: f'R$ {x:.2f}')

grafico = make_subplots(
    rows=3, cols=1,
    subplot_titles=("Total gasto comprando cada produto", 
                    "Total ganho vendendo cada produto", 
                    "Gastos VS ganhos no período")
)

grafico.add_trace(
    go.Bar(x=dados_agrupados_entradas['nomeProduto'], y=dados_agrupados_entradas['valorTotal'], 
           text=dados_agrupados_entradas['valorTotalFormatado'], 
           textposition='auto',
           name="Total gasto"),
    row=1, col=1
)

grafico.add_trace(
    go.Bar(x=dados_agrupados_saidas['nomeProduto'], y=dados_agrupados_saidas['valorTotal'], 
           text=dados_agrupados_saidas['valorTotalFormatado'], 
           textposition='auto', 
           name="Total ganho"),
    row=2, col=1
)

dados_comparar = pd.merge(dados_agrupados_entradas, dados_agrupados_saidas, on='nomeProduto', suffixes=('_Entrada', '_Saida'))
dados_comparar['valorTotal_Entrada_Formatado'] = dados_comparar['valorTotal_Entrada'].apply(lambda x: f'R$ {x:.2f}')
dados_comparar['valorTotal_Saida_Formatado'] = dados_comparar['valorTotal_Saida'].apply(lambda x: f'R$ {x:.2f}')

grafico.add_trace(
    go.Bar(x=dados_comparar['nomeProduto'], y=dados_comparar['valorTotal_Entrada'], 
           text=dados_comparar['valorTotal_Entrada_Formatado'], 
           textposition='auto', 
           name="Total gasto (Entrada)"),
    row=3, col=1
)
grafico.add_trace(
    go.Bar(x=dados_comparar['nomeProduto'], y=dados_comparar['valorTotal_Saida'], 
           text=dados_comparar['valorTotal_Saida_Formatado'], 
           textposition='auto', 
           name="Total ganho (Saída)"),
    row=3, col=1
)
grafico.update_layout(
    height=900, 
    title_text="Análise de Compras e Vendas de Produtos",
    barmode='group', 
)
grafico.show()

dados_vendas = dados_agrupados_saidas.copy()
dados_vendas = dados_vendas.sort_values(by='valorTotal', ascending=False)
dados_vendas['valorTotalFormatado'] = dados_vendas['valorTotal'].apply(lambda x: f'R$ {x:.2f}')
dados_vendas['textoBarra'] = dados_vendas['valorTotalFormatado'] + ' vendidos no período'

grafico_vendas = px.bar(dados_vendas, 
                   x='nomeProduto', 
                   y='valorTotal', 
                   title='Análise de Produtos: Mais e Menos Vendidos',
                   labels={'nomeProduto': 'Produto', 'textoBarra': 'Total vendido no período'},
                   hover_data={'valorTotal':False},
                   text='textoBarra',  
                   color='valorTotal')

grafico_vendas.update_layout(hovermode='closest')
grafico_vendas.update_traces(textposition='none')  
grafico_vendas.show()