import streamlit as st
import requests

def login_page():
    st.title("Страница входа")

    username = st.text_input("Имя пользователя")
    password = st.text_input("Пароль", type="password")

    if st.button("Войти"):
        if username and password:
            response = requests.post(
                'http://127.0.0.1:8000/api/custom-login/',
                json={
                    'username': username,
                    'password': password
                })
            if response.status_code == 200:
                token = response.json().get('token')
                st.session_state['token'] = token
                st.session_state['logged_in'] = True
                st.success("Вход выполнен успешно!")
                st.switch_page("pages/Records.py")
            else:
                st.error("Неверное имя пользователя или пароль.")
        else:
            st.error("Заполните все поля.")

if __name__ == "__main__":
    login_page()