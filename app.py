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
    Este site foi desenvolvido para oferecer desafios práticos de SQL,
    compondo a parte aplicada do *Curso de SQL com Aplicação a Problemas de Negócios*.

    O objetivo do curso é ensinar os fundamentos da linguagem SQL,
    capacitando os estudantes a compreender e utilizar suas principais funções
    e, além disso, aplicá-los na *resolução de problemas **reais** de negócio*.
                    
    A iniciativa é do Grupo de Processamento e Análise de Dados (PANDA)
    da Universidade Federal de São Carlos (UFSCar) e busca integrar teoria e prática,
    desenvolvendo raciocínio analítico e habilidades essenciais em manipulação e
    análise de dados.

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

def rodape():
    st.markdown("""
        <style>
            .footer-space {
                height: 80px;  /* reserva espaço para o rodapé */
            }

            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: var(--background-color);
                border-top: 1px solid rgba(150,150,150,0.2);
                text-align: center;
                padding: 15px;
                font-size: 0.85rem;
                color: #6c757d;
                backdrop-filter: blur(6px);
            }

            .footer a {
                text-decoration: none;
                margin: 0 10px;
            }

            .footer a:hover {
                text-decoration: underline;
            }
        </style>

        <div class="footer-space"></div>

        <div class="footer">
            Desenvolvido por <strong>Lucas Battisti</strong>
            <br>
            <a href="https://github.com/lucas-battisti" target="_blank">🐙 GitHub</a>
            <a href="https://linkedin.com/in/lucas-battisti" target="_blank">🔗 LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)

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

if pagina_selecionada == "Home":
    rodape()