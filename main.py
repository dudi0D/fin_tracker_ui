import streamlit as st


st.title('Добро пожаловать в приложение!')

st.markdown(
    """
    <h3 style='color: #4CAF50;'>Пожалуйста, выберите действие:</h3>
    """,
    unsafe_allow_html=True
)

st.page_link("pages/Register.py", label="🔑 Регистрация", icon="🔑")
st.page_link("pages/Login.py", label="🔒 Вход", icon="🔒")
