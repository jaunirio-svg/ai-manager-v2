import streamlit as st
import google.generativeai as genai

# Configuração da página para notebook e celular
st.set_page_config(page_title="AI Manager", layout="wide")

# Conecta com a sua chave de segurança
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Chave API não configurada nos Secrets do Streamlit.")

st.title("📱 AI Assistant Manager")

# Menu de navegação
menu = st.sidebar.selectbox("Menu", ["Gerar Conteúdo", "Dashboard"])

if menu == "Gerar Conteúdo":
    st.subheader("O que vamos criar hoje?")
    tema = st.text_input("Digite o tema ou produto:")
    
    if st.button("Gerar com IA"):
        if tema:
            with st.spinner('A IA está trabalhando...'):
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(tema)
                st.success("Pronto!")
                st.write(response.text)
        else:
            st.warning("Por favor, digite um tema primeiro.")

elif menu == "Dashboard":
    st.info("Suas métricas aparecerão aqui conforme você usar o app.")
