import streamlit as st

st.title('Simulador de créditos')

rate_type = st.selectbox("Tipo de tasa", ("Mensual", "Anual"))
amount = st.number_input(
    "Valor del préstamo",
    value=100_000_000,
    min_value=0,
    format="%d",
)
rate = st.number_input(
    "Tasa de interés (Ej: 10, 15, 0.5)",
    value=0.833,
    step=0.001,
    min_value=0.0,
    format="%f",
)
months = st.number_input(
    "Plazo en meses",
    value=180,
    min_value=1,
)
insurance = st.number_input(
    "Seguro mensual de deuda",
    value=0,
    min_value=0,
    format="%d",
)
# coin = st.selectbox("Divisa", ("COP", "USD"))

rate /= 100

if rate_type == "Anual":
    rate = (1 + rate) ** (1 / 12) - 1

#years = 12 * years

result = (rate * amount) / (1 - (1 / (1 + rate) ** months))

st.header(f"Cuota mensual : $ {round(result + insurance):,.0f}")
