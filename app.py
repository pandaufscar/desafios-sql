import streamlit as st

from desafio import exibir_desafio_sql

import desafios.fundamentos as fundamentos

st.set_page_config(
    page_title="Desafios SQL",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .block-container {
            max-width: 900px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================
# PÁGINAS (FUNÇÕES)
# =====================================================

def pagina_home():
    col1, col2 = st.columns([4, 1])  # ajusta proporção conforme necessário

    with col1:
        st.title("Desafios SQL")
        st.markdown("""
    Este site foi desenvolvido com o objetivo de oferecer **desafios interativos**
    para o *Curso de SQL com Aplicação a Problemas de Negócios*.

    O curso é uma iniciativa do **Grupo de Processamento e ANálise de DAdos (PANDA)**
    da UFSCar e tem como foco aplicar consultas SQL na resolução de problemas
    reais de negócio, desenvolvendo raciocínio analítico e habilidades práticas
    em manipulação de dados.

    Utilize a barra lateral para navegar entre os desafios!

    🔗 Saiba mais sobre o grupo:  
    [Grupo de Processamento e Análise de Dados - UFSCar](linktr.ee/pandaufscar)
    """)

    with col2:
        st.image("logo.png", width=120)

    st.divider()

    st.markdown("""
              # Base de dados  
                """)
    
    st.image("schema.png")

def pagina_fundamentos():
    st.header("Módulo: Fundamentos")

    desafio = st.selectbox(
        "Escolha o desafio:",
        [dic["titulo"] for dic in fundamentos.dics]
    )

    desafio_dict = next(
    d for d in fundamentos.dics
    if d["titulo"] == desafio
    )

    exibir_desafio_sql(desafio_dict)

def pagina_joins():
    st.header("Módulo: Joins")
    st.write("Aqui ficarão os exercícios de JOIN.")

def pagina_agregacoes():
    st.header("Módulo: Agregações")
    st.write("Aqui ficarão os exercícios de GROUP BY, HAVING etc.")

# =====================================================
# MAPA DE ROTAS
# =====================================================

ROTAS = {
    "Home": pagina_home,
    "Fundamentos": pagina_fundamentos,
    "Joins": pagina_joins,
    "Agregações": pagina_agregacoes,
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Escolha um módulo:")

pagina_selecionada = st.sidebar.radio(
    "",
    list(ROTAS.keys())
)

# =====================================================
# ROTEAMENTO
# =====================================================

ROTAS[pagina_selecionada]()