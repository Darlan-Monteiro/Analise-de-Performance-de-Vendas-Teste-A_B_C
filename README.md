# 📊 Análise de Performance de Vendas & Teste A/B

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-green)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow)
![Figma](https://img.shields.io/badge/Figma-UI%2FUX-purple)

## 💼 Sobre o Projeto

Este projeto consiste em uma análise completa de dados (**End-to-End Data Analytics**) simulando um cenário real de e-commerce. O objetivo principal foi validar os resultados de um **Teste A/B** aplicado a três grupos de clientes, além de investigar padrões de vendas, geografia e comportamento de cancelamento.

O diferencial deste projeto está na etapa rigorosa de **Engenharia de Dados (ETL)**, onde dados brutos com inconsistências de cadastro e taxonomia foram tratados antes da geração de inteligência.

---

## 🖼️ Visualização (Dashboard)

![Preview do Dashboard](images/dashboard_preview.png)
<img width="1350" height="753" alt="image" src="https://github.com/user-attachments/assets/6acf4fdb-4e67-4290-b274-51e37c7c75ea" />


> **Destaque Visual:** O layout do Dashboard foi prototipado no **Figma** para garantir uma hierarquia visual executiva, facilitando a leitura dos KPIs principais.

---

## 🎯 Perguntas de Negócio Resolvidas

1.  **Qual grupo deve ser escolhido (A, B ou C)?**
    * **Resposta:** Grupo B.
    * **Insight:** Apesar do volume de vendas ser equilibrado, o Grupo B apresentou um **Ticket Médio significativamente superior (R$ 3.380)**, gerando a maior receita total confirmada.

2.  **A localização influencia o valor da venda?**
    * **Insight:** Estados como MG e RR concentram maior volume, mas o Ticket Médio se mantém estável nacionalmente. A geografia impacta conversão, não o valor gasto.

3.  **A Categoria do produto influencia o cancelamento?**
    * **Insight:** Não. A taxa de cancelamento se mantém uniforme (~16%) independente da categoria (Eletrônicos, Roupas, etc.), indicando que o problema não é o produto, mas possivelmente logística ou meio de pagamento.

---

## 🛠️ Ferramentas & Tecnologias

* **Python (Pandas & PandasQL):** Utilizado para limpeza de dados (ETL), correção de strings (`sao Paulo` -> `SÃO PAULO`), unificação de categorias e tratamento de datas.
* **SQL:** Utilizado dentro do ambiente Python para validação de hipóteses e agregações complexas.
* **Power BI:** Construção do Dashboard interativo e cálculo de medidas DAX (Ticket Médio, Taxa de Cancelamento).
* **Figma:** Design de interface (UI) e background do relatório.

---

## 🗂️ Estrutura do Pipeline (ETL)

O script `processamento.py` realiza as seguintes etapas:
1.  **Ingestão:** Leitura dos arquivos CSV brutos (Clientes, Pedidos, Itens, Produtos).
2.  **Sanitização:**
    * Correção de nomes de cidades e estados.
    * Padronização de categorias (ex: `Decoração`, `Decoracao` -> `DECORAÇÃO`).
    * Tratamento de status de pedidos (`Pending` -> `PENDENTE`).
3.  **Modelagem:** Criação de uma Tabela Fato consolidada (*Flat Table*) unindo as 4 fontes de dados.
4.  **Exportação:** Geração de arquivo `.csv` otimizado para leitura no Power BI (separador `;` e decimais com `,`).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.x
* Bibliotecas: `pandas`, `pandasql`


# Instale as dependências
pip install pandas pandasql
