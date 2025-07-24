import streamlit as st
import requests

def registration_page():
    st.title("Страница регистрации")

    username = st.text_input("Имя пользователя")
    email = st.text_input("Email")
    password = st.text_input("Пароль", type="password")
    confirm_password = st.text_input("Подтвердите пароль", type="password")

    if st.button("Зарегистрироваться"):
        if not username or not email or not password or not confirm_password:
            st.error("Пожалуйста, заполните все поля.")
        elif "@" not in email or "." not in email:
            st.error("Введите корректный email.")
        elif password != confirm_password:
            st.error("Пароли не совпадают.")
        else:
            response = requests.post(
                'http://127.0.0.1:8000/api/register/',
                json={
                    'username': username,
                    'email': email,
                    'password': password
                }
            )
            if response.status_code == 201:
                st.success("Регистрация прошла успешно!")
                st.success(f"Пользователь {username} успешно зарегистрирован!")
                token = response.json().get('token')
                st.session_state['token'] = token
                st.session_state['logged_in'] = True
                st.success("Вход выполнен успешно!")
                st.switch_page("pages/Records.py")
            else:
                st.error("Ошибка регистрации. Попробуйте снова.")

if __name__ == "__main__":
    registration_page()