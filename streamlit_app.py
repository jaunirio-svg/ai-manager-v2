import streamlit as st
import google.generativeai as genai

# Configuração para celular e PC
st.set_page_config(page_title="AI Manager", layout="wide")

# Conecta com a chave que você colou nos Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Chave API não encontrada. Vá em Settings > Secrets e adicione GEMINI_API_KEY")

st.title("📱 AI Assistant Manager")

# Este é o modelo 'gemini-pro', que é o mais compatível com o plano gratuito
try:
    model = genai.GenerativeModel('gemini-1.0-pro')
except:
    st.error("Erro ao carregar o modelo. Verifique sua chave API.")

tema = st.text_input("Sobre o que quer escrever?", placeholder="Ex: Roteiro para medalha...")

if st.button("Gerar com IA"):
    if tema:
        with st.spinner('Aguarde...'):
            try:
                response = model.generate_content(tema)
                st.markdown("### Resultado:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro na geração: {e}")
    else:
        st.warning("Por favor, digite um tema.")
