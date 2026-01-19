import pandas as pd
from pandasql import sqldf

def importar_dados():
    clientes = pd.read_csv('clientes.csv')
    itens_pedido = pd.read_csv('itens_pedido.csv')
    pedidos = pd.read_csv('pedidos.csv')
    produtos = pd.read_csv('produtos.csv')
    return clientes, itens_pedido, pedidos, produtos

def limpar_dados(clientes, pedidos, produtos):
    # limpando dados da tabela produtos
    produtos['categoria'] = (
        produtos['categoria']
        .replace('Eletronicos', 'Eletrônicos')
        .replace('Eletrodomesticos', 'Eletrodomésticos')
        .replace('Moveis', 'Móveis')
        .replace('Utensilios', 'Utensílios')
        .replace('Decoracao', 'Decoração')
        .replace('Decoraçao', 'Decoração'))

    # limpando dados da tabela clientes
    clientes['cidade'] = (
        clientes['cidade']
        .replace('sao Paulo','Sao Paulo')
        .replace('Sao Paulo','São Paulo')
        .replace('Rio', 'Rio de Janeiro')
        .replace('Maranhao', 'Maranhão')
        .replace('Goiania', 'Goiânia'))
 
    # limpando dados da tabela pedidos
    pedidos['status'] = pedidos['status'].replace('Pending','Pendente')
    
    # deixando todas as informações das colunas em maiúsculo
    pedidos['status'] = pedidos['status'].str.upper()
    produtos['categoria'] = produtos['categoria'].str.upper()
    clientes['cidade'] = clientes['cidade'].str.upper()
    
    # conversão de datas para novo bd
    clientes['data_cadastro'] = pd.to_datetime(clientes['data_cadastro'])
    pedidos['data_pedido'] = pd.to_datetime(pedidos['data_pedido'])
    
    return clientes, pedidos, produtos

def gerar_arquivo_consolidado(clientes, itens_pedido, pedidos, produtos):
    
    df_consolidado = pd.merge(itens_pedido, pedidos, on='pedido_id', how='inner')
    
    df_consolidado = pd.merge(df_consolidado, produtos, on='produto_id', how='left')
    
    df_consolidado = pd.merge(df_consolidado, clientes, on='cliente_id', how='left')
    
    
    colunas_finais = [
        'pedido_id', 
        'data_pedido', 
        'status', 
        'cliente_id', 
        'nome',         
        'cidade', 
        'estado', 
        'grupo', 
        'categoria', 
        'produto_id', 
        'quantidade', 
        'preco_unitario', 
        'subtotal'     
    ]
    
    df_final = df_consolidado[colunas_finais].copy()
    
    df_final = df_final.rename(columns={
        'nome': 'nome_cliente',
        'subtotal': 'valor_item_total'
    })
    
    nome_arquivo = 'base_consolidada_powerbi.csv'
    df_final.to_csv(nome_arquivo, index=False, sep=';', encoding='utf-8-sig', decimal=',')
    
    print(f"Sucesso! Arquivo '{nome_arquivo}' gerado na pasta.")

def main():
    clientes, itens_pedido, pedidos, produtos = importar_dados()
    
    clientes, pedidos, produtos = limpar_dados(clientes, pedidos, produtos)
    
    gerar_arquivo_consolidado(clientes, itens_pedido, pedidos, produtos)
    
    return clientes, itens_pedido, pedidos, produtos

if __name__ == "__main__":
    clientes, itens_pedido, pedidos, produtos = main()