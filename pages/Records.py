import streamlit as st
import requests
import pandas as pd


if not st.session_state.get('logged_in'):
    st.warning("Сначала войдите в систему.")
    st.stop()

st.title("Страница транзакций")
response = requests.get(
    'http://127.0.0.1:8000/api/records/',
    headers={
        'Authorization': f'Token {st.session_state.get("token")}'
    }
)
data = response.json()
if not data:
    st.markdown(
        """
        <h3 style='color: #4CAF50;'>Здесь будут отображаться ваши транзакции</h3>
        """,
        unsafe_allow_html=True
    )
    st.stop()
else:
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    gain_sum = df[df['type'] == 'GAIN']['size'].astype(float).sum()
    loss_sum = df[df['type'] != 'GAIN']['size'].astype(float).sum()
    total = gain_sum + loss_sum

    if total > 0:
        st.pyplot(
            pd.Series(
                [gain_sum, loss_sum],
                index=['Доход', 'Расход']
            ).plot.pie(
                autopct='%1.1f%%',
                colors=['#4CAF50', '#FF5252'],
                ylabel=''
            ).get_figure()
        )
    if st.button('Добавить транзакцию'):
        st.session_state['new_transaction'] = True
        st.switch_page('pages/NewRecord.py')
    current_balance = gain_sum - loss_sum
    st.markdown(
        f"""
        <h3 style='color: #4CAF50;'>Текущий баланс: {current_balance:.2f} руб.</h3>
        """,
        unsafe_allow_html=True
    )