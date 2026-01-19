import pandas as pd
from pandasql import sqldf
from processamento import main

def executar_sql(query):
    return sqldf(query, globals())

clientes, itens_pedido, pedidos, produtos = main()

# questão 1:
q1 = """
SELECT 
    c.grupo,
    COUNT(DISTINCT c.cliente_id) as qtd_clientes,
    COUNT(DISTINCT p.pedido_id) as qtd_vendas_confirmadas,
    SUM(p.valor_total) as receita_total,
    AVG(p.valor_total) as ticket_medio
FROM 
    clientes c
JOIN 
    pedidos p ON c.cliente_id = p.cliente_id
WHERE
    p.status = 'CONFIRMADO'
GROUP BY 
    c.grupo
ORDER BY 
    receita_total DESC
"""

df_resultado_q1 = executar_sql(q1)

pd.options.display.float_format = '{:,.2f}'.format
print(df_resultado_q1)

# questão 2:
q2 = """
SELECT 
    c.estado,
    COUNT(DISTINCT p.pedido_id) as qtd_vendas,
    SUM(p.valor_total) as receita_total,
    AVG(p.valor_total) as ticket_medio
FROM 
    clientes c
JOIN 
    pedidos p ON c.cliente_id = p.cliente_id
WHERE
    p.status = 'CONFIRMADO'
GROUP BY 
    c.estado
ORDER BY 
    receita_total DESC
"""

df_resultado_q2 = executar_sql(q2)
print(df_resultado_q2.head(10))


# questão 3:
q3 = """
SELECT 
    c.cidade,
    SUM(p.valor_total) as receita_total,
    COUNT(DISTINCT p.pedido_id) as qtd_vendas
FROM 
    clientes c
JOIN 
    pedidos p ON c.cliente_id = p.cliente_id
WHERE
    p.status = 'CONFIRMADO'
GROUP BY 
    c.cidade
ORDER BY 
    receita_total DESC
"""

df_resultado_q3 = executar_sql(q3)
print(df_resultado_q3.head(10))

# questão 4:
# categoria x status
q4_categoria = """
SELECT 
    prod.categoria,
    p.status,
    COUNT(DISTINCT p.pedido_id) as qtd_pedidos
FROM 
    pedidos p
JOIN 
    itens_pedido i ON p.pedido_id = i.pedido_id
JOIN 
    produtos prod ON i.produto_id = prod.produto_id
GROUP BY 
    prod.categoria, p.status
ORDER BY 
    prod.categoria, p.status
"""

df_resultado_q4_cat = executar_sql(q4_categoria)
print(df_resultado_q4_cat)


# quantidade x status
q4_quantidade = """
SELECT 
    p.status,
    AVG(i.quantidade) as media_qtd_itens_por_pedido
FROM 
    pedidos p
JOIN 
    itens_pedido i ON p.pedido_id = i.pedido_id
GROUP BY 
    p.status
ORDER BY 
    media_qtd_itens_por_pedido DESC
"""

df_resultado_q4_qtd = executar_sql(q4_quantidade)
print(df_resultado_q4_qtd)
