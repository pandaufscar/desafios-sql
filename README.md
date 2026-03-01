# Plataforma Interativa de Desafios de SQL

Este projeto foi desenvolvido para oferecer desafios práticos de SQL, compondo a parte aplicada do Curso de SQL com Aplicação a Problemas de Negócios. O objetivo do curso é ensinar os fundamentos da linguagem SQL, capacitando os estudantes a compreender e utilizar suas principais funções e, além disso, aplicá-los na resolução de problemas reais de negócio. A iniciativa é do [Grupo de Processamento e Análise de Dados (PANDA)](linktr.ee/pandaufscar) da Universidade Federal de São Carlos (UFSCar) e busca integrar teoria e prática, desenvolvendo raciocínio analítico e habilidades essenciais em manipulação e análise de dados.

A implementação da plataforma e o desenvolvimento técnico do projeto foram realizados pelo membro **Lucas Battisti** ([@lucas-battisti](https://github.com/lucas-battisti)).

🔗 **Acesse a plataforma online:**  
https://desafios-sql.streamlit.app/

## 🚀 Funcionalidades:

- **Foco em problemas reais de negócio**: Exercícios baseados em situações práticas, aproximando o aluno do mercado.
- **Feedback instantâneo**: Indicação clara de acerto ou erro para acelerar o aprendizado, assim, o aluno aprende fazendo, testando e ajustando suas consultas.
- **Validação inteligente**: Compara a reposta do aluno com o esperado ignorando detalhes irrelevantes como: nome e ordem das colunas ou linhas.
- **Visualização do esquema do banco**: Acesso ao diagrama da base de dados, facilitando a compreensão das tabelas, chaves e relacionamentos antes da construção das consultas.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem utilizada.
- **Streamlit**: Para a interface web interativa.
- **Pandas**: Manipulação e comparação de dados.
- **SQLite3**: Banco de dados local.

## 📁 Estrutura do Projeto

```bash
plataforma-sql-panda/
├── app.py                  # ← Arquivo principal (Streamlit)
├── desafio.py              # ← Lógica de exibição, execução e validação
├── fundamentos.py          # ← Desafios do módulo Fundamentos
├── joins.py                # ← Desafios do módulo Joins (exemplo)
├── agregacoes.py           # ← Desafios do módulo Agregações (exemplo)
├── dados/
│   └── dados.db            # ← Banco SQLite com todos os dados
├── schema.png              # ← Diagrama do banco (usado na interface)
├── requirements.txt
└── README.md
```

## ✅ TO-DO

- Melhorar design das páginas de módulos
- Atualizar esquema do banco de dados e adicionar ao README
- Adicionar mais exercícios
- Melhorar requirements.txt
