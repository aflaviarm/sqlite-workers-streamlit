# Análise de Funcionários com SQLite + Streamlit

Este projeto cria um banco de dados SQLite com dados fictícios de funcionários e fornece uma interface visual para analisar os dados.

## Funcionalidades

- Criação automática do banco `company.db`.
- Tabela `workers` com dados como nome, cargo, salário e data de admissão.
- Consultas SQL para:
  - Cargos únicos.
  - Top 5 maiores salários.
  - Top 5 menores salários.
  - Média salarial por cargo.
  - Maiores salários por cargo.
- Interface interativa via Streamlit.


## Estrutura do Projeto

````

├── app.py                   # Interface Streamlit (chama o módulo do banco de dados)
├── create_and_query_db.py   # Módulo com lógica SQL e criação do banco de dados
├── requirements.txt         # Dependências do projeto
└── README.md                  

````

> O arquivo `company.db` será criado automaticamente ao rodar o aplicativo.


## Requisitos

- Python 3.7 ou superior.
- Pip.


## Instalação


1. Clone o repositório:
```bash
git clone https://github.com/aflaviarm/sqlite-workers-streamlit.git
cd sqlite-workers-streamlit
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a interface:

```bash
streamlit run app.py
```

ou

```bash
python -m streamlit run app.py
```

## Sobre o funcionamento

* Ao iniciar o app (`app.py`), o módulo `create_and_query_db.py`:

  * Cria (ou recria) o banco `company.db`.
  * Insere todos os dados fictícios.
  * Executa as consultas SQL.
  * Retorna os resultados como DataFrames para o Streamlit exibir.


## Observações

* A interface será aberta automaticamente no navegador padrão.
* Todos os dados são fictícios.

---

> Desenvolvido por Ana Flávia Regis Macêdo.
