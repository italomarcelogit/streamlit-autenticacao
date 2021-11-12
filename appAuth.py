# CREDITO AO STREAMLIT_AUTHENTICATOR: M Khorasani / git: @mkhorasani

import streamlit as st
import streamlit_authenticator as stauth
import socket  
import os


os.system('clear')
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)   
st.set_page_config(page_title='Auth', layout='wide')


nomes = ['Italo', 'Marcelo']
usuarios = ['Italo', 'Marcelo']
senhas = ['italo', 'marcelo']
senhas_cripto = stauth.hasher(senhas).generate()
print('Exemplo das criptografias', senhas_cripto)


def menu():
    st.sidebar.header("Menu")
    v = st.sidebar.slider('Escolha um valor', 10, 20, 16)
    return v


def login():
    autenticador = stauth.authenticate(nomes, usuarios, senhas_cripto, 'nome_cookie', 'chave_cookie', cookie_expiry_days=2)
    nome, status = autenticador.login('Login', 'main')
    return nome, status
    

def main():
    st.title(f'Olá {usuarioLogado}')
    st.write(f'Conteúdo do usuário logado - {str(valor)}')


def ocultaRodape():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == '__main__':
    ocultaRodape()
    usuarioLogado, logado = login()
    if logado:
        valor = menu()
        main()
    elif logado == False:
        st.error('Usuário ou senha incorreta')
    else:
        st.warning('Digite seu login e sua senha')
