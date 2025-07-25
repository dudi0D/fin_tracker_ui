import streamlit as st
import requests


if not st.session_state.get('new_transaction'):
    st.warning('Пожалуйста, сначала добавьте транзакцию на странице "Транзакции".')
    st.stop()
st.title("Добавление новой транзакции")
st.markdown(
    """
    <h3 style='color: #4CAF50;'>Пожалуйста, заполните форму для добавления новой транзакции:</h3>
    """,
    unsafe_allow_html=True
)
type_choice = [(i, i.upper()) for i in ['Gain', 'Loss']]
sphere_choice = [(i, i.upper()) for i in ['', 'Housing', 'Food', 'Transport', 'Enjoyment', 'Deposit']]
currency_choice = [(i, i.upper()) for i in ['usd', 'eur', 'rub']]
type_selected = st.selectbox(
    "Тип транзакции",
    options=[x[0] for x in type_choice],
    format_func=lambda x: dict(type_choice)[x]
)
size = st.number_input("Сумма", min_value=0.0, step=0.01)
sphere_selected = st.selectbox(
    "Сфера",
    options=[x[0] for x in sphere_choice],
    format_func=lambda x: dict(sphere_choice)[x]
)
currency_selected = st.selectbox(
    "Валюта",
    options=[x[0] for x in currency_choice],
    format_func=lambda x: dict(currency_choice)[x]
)
if st.button("Добавить транзакцию"):
    response = requests.post(
        'http://127.0.0.1:8000/api/records/',
        headers={
            'Authorization': f'Token {st.session_state.get("token")}',
            'Content-Type': 'application/json'
        },
        json={
            'type': type_selected.upper(),
            'size': size,
            'sphere': sphere_selected.upper(),
            'currency': currency_selected.upper()
        }
    )
    if response.status_code == 201:
        st.success(f"Транзакция добавлена: {type_selected}, {size}, {sphere_selected}, {currency_selected}")
    else:
        st.error("Ошибка при добавлении транзакции. Пожалуйста, попробуйте еще раз.")