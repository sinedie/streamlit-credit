import streamlit as st

rate_type = st.selectbox("Tipo de tasa", ("Mensual", "Anual"))
amount = st.number_input(
    "Valor del préstamo",
    value=100_000_000,
    min_value=0,
    format="%d",
)
rate = st.number_input(
    "Tasa de interés",
    value=0.833,
    step=0.001,
    min_value=0.0,
    format="%f",
)
years = st.number_input(
    "Plazo en años",
    value=15,
    min_value=1,
)
insurance = st.number_input(
    "Seguro",
    value=0,
    min_value=0,
    format="%d",
)
coin = st.selectbox("Divisa", ("COP", "USD"))


if rate_type == "Anual":
    rate = (1 + rate) ** 1 / 12 - 1

years = 12 * years
rate /= 100
result = (rate * amount) / (1 - (1 / (1 + rate) ** years))

st.header(f"Total : $ {round(result + insurance):,.0f} {coin}")
