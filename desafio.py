import streamlit as st
import pandas as pd
import sqlite3

def validar_resposta(
    df_usuario: pd.DataFrame,
    df_resposta: pd.DataFrame,
    ordem_linhas: bool = False
) -> bool:
    """
    Compara dois DataFrames
    
    Parameters
    ----------
    df_usuario : DataFrame retornado pelo aluno
    df_resposta : DataFrame esperado
    ordem_linhas : bool
        Se True, a ordem das linhas deve ser igual.
        Se False, a ordem das linhas será ignorada.
    """

    # Resetar índices
    df_u = df_usuario.reset_index(drop=True).copy()
    df_r = df_resposta.reset_index(drop=True).copy()

    # Testa mesma dimensão
    if df_u.shape[1] != df_r.shape[1]:
        return False
    
    # Percorre todas as colunas da resposta, até achar alguma igual,
    #       ignorando os nomes das colunas,
    #       mas levado em consideração a ordem das linhas. 
    if ordem_linhas:
        for col_r in df_r.columns:

            encontrou_coluna = False

            for col_u in df_u.columns:

                if df_r[col_r].equals(df_u[col_u]):
                    encontrou_coluna = True
                    break


            if not encontrou_coluna:
                return False
            
    # Percorre todas as colunas da resposta, até achar alguma igual,
    #       ignorando os nomes das colunas,
    #       mas levado em consideração a ordem das linhas. 
    if ordem_linhas:
        for col_r in df_r.columns:

            encontrou_coluna = False

            for col_u in df_u.columns:

                if df_r[col_r].reset_index(drop=True).equals(df_u[col_u].reset_index(drop=True)):
                    encontrou_coluna = True
                    break


            if not encontrou_coluna:
                return False
            
    # Percorre todas as colunas da resposta, até achar alguma igual,
    #       ignorando os nomes das colunas,
    #       ignorando a ordem das linhas.        
    else:
        for col_r in df_r.columns:

            encontrou_coluna = False

            for col_u in df_u.columns:

                # ordena para ignorar ordem das linhas
                if df_r[col_r].sort_values().reset_index(drop=True).equals(df_u[col_u].sort_values().reset_index(drop=True)):
                    encontrou_coluna = True
                    break


            if not encontrou_coluna:
                return False
            
    return True          

   

def exibir_desafio_sql(dic):
    """
    dic: dict com as chaves:
        - titulo: str
        - enunciado: str
        - imagem_esquema: str (caminho da imagem)
        - resposta_sql: str
        - ordem: bool
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
                if validar_resposta(df, resposta_df, dic['ordem']):
                    st.success("✅ Parabéns! Você acertou o desafio!")
                    st.dataframe(df)
                else:
                    st.error("❌ Ops! Tente novamente.")
                    st.dataframe(df)
            except Exception as e:
                st.error(f"Erro ao executar SQL: {e}")