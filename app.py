"""
app.py

Interface interativa usando Streamlit para exibir análises sobre
os funcionários da empresa contidos no banco de dados company.db.

Autor: Ana Flávia Regis Macêdo
"""

import streamlit as st
import create_and_query_db as db

def format_salario(df, colunas=None):
    """
    Formata colunas numéricas no estilo brasileiro: 6.200,00
    Args:
        df (pd.DataFrame): DataFrame a ser formatado.
        colunas (list): lista de nomes de colunas a formatar.
    Returns:
        pd.DataFrame: DataFrame com colunas formatadas.
    """
    if colunas is None:
        colunas = [col for col in df.columns if 'Salário (R$)' in col or 'Média Salarial (R$)' in col]

    df_format = df.copy()
    for col in colunas:
        if col in df_format.columns:
            df_format[col] = df_format[col].apply(
                lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            )
    return df_format


def connect_db():
    """
    Conecta ao banco SQLite e retorna um DataFrame contendo os resultados das consultas ao banco.

    Returns:
        pd.DataFrame: resultados das consultas ao banco.
    """
    connection = db.create_and_populate()
    results = db.run_queries(connection)

    connection.close()

    return results

def show_queries(results):
    """
    Exibe os dados e estatísticas na interface do Streamlit.

    Args:
        results (pd.DataFrame): resultados das consultas ao banco.
    """
    st.set_page_config(page_title="Análise de Funcionários", layout="wide")

    st.title("Análise de Funcionários")
    st.write("Os dados abaixo são baseados em um banco SQLite gerado com dados fictícios.")

    st.header("1️⃣ Cargos únicos")
    st.write(f"Total: {len(results['unique_roles'])} cargos únicos")
    st.dataframe(
        results["unique_roles"].rename(columns={
            "cargo": "Cargo"
        }), hide_index=True)

    st.header("2️⃣ Top 5 maiores salários")
    st.dataframe(format_salario(
        results["top_salaries"].rename(columns={
            "nome": "Nome",
            "cargo": "Cargo",
            "salario": "Salário (R$)"
        })), hide_index=True)

    st.header("3️⃣ Top 5 menores salários")
    st.dataframe(format_salario(
        results["lowest_salaries"].rename(columns={
            "nome": "Nome",
            "cargo": "Cargo",
            "salario": "Salário (R$)"
        })), hide_index=True)

    st.header("4️⃣ Média salarial por cargo")
    st.dataframe(format_salario(
        results["avg_salary_by_role"].rename(columns={
            "nome": "Nome",
            "media": "Média Salarial (R$)"
        })), hide_index=True)

    st.header("5️⃣ Maiores salários por cargo")
    st.dataframe(format_salario(
        results["top_earner_per_role"].rename(columns={
            "nome": "Nome",
            "cargo": "Cargo",
            "salario": "Salário (R$)"
        })), hide_index=True)

if __name__ == "__main__":
    results = connect_db()
    show_queries(results)
