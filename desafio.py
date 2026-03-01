import streamlit as st
import pandas as pd
import sqlite3

def exibir_desafio_sql(dic):
    """
    dic: dict com as chaves:
        - titulo: str
        - enunciado: str
        - imagem_esquema: str (caminho da imagem)
        - resposta_sql: str
    """

    st.header("💻 Desafio: " + dic['titulo'])

    # enunciado
    st.write(dic['enunciado'])

    # ---------- BOTÃO POP-UP COM IMAGEM ----------
    with st.expander("📊 Ver esquema da base"):
        st.image(dic['imagem_esquema'], caption="Esquema da Base de Dados")
        

    # --------------- RESPOSTA ---------------

    conn = sqlite3.connect("dados/dados.db")

    resposta_df = pd.read_sql_query(dic['resposta_sql'], conn)

    conn.close()

    # ---------- DUAS COLUNAS ----------
    col1, col2 = st.columns(2)

    # Coluna 1: Editor SQL
    with col1:
        st.subheader("Escreva seu código SQL:")
        input_sql = st.text_area("SQL", height=200)
        executar = st.button("🚀 Executar SQL", key=f"executar_{dic['titulo']}")

    # Coluna 2: Output / Resultados
    with col2:
        st.subheader("Resultado e Validação")
        if 'executar' in locals() and executar:
            try:
                conn = sqlite3.connect("dados/dados.db")

                df = pd.read_sql_query(input_sql, conn)
                conn.close()

                # ---------- VALIDAÇÃO ----------
                if df.reset_index(drop=True).equals(resposta_df):
                    st.success("✅ Parabéns! Você acertou o desafio!")
                    st.dataframe(df)
                else:
                    st.error("❌ Ops! Tente novamente.")
                    st.dataframe(df)
            except Exception as e:
                st.error(f"Erro ao executar SQL: {e}")