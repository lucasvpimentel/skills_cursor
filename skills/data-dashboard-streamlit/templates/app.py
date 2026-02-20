import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Data Dashboard", layout="wide")

@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.DataFrame({
        "category": ["A", "A", "B", "B", "C", "C"],
        "value": [10, 12, 7, 9, 3, 5],
        "date": pd.to_datetime(["2026-01-01","2026-01-02","2026-01-01","2026-01-02","2026-01-01","2026-01-02"])
    })

df = load_data()

st.title("📊 Data Dashboard (Streamlit + Plotly)")

with st.sidebar:
    st.header("Filtros")
    categories = st.multiselect("Categoria", sorted(df["category"].unique()), default=sorted(df["category"].unique()))
    date_min = df["date"].min().date()
    date_max = df["date"].max().date()
    date_range = st.date_input("Período", value=(date_min, date_max), min_value=date_min, max_value=date_max)

d1, d2 = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
f = df[df["category"].isin(categories)]
f = f[(f["date"] >= d1) & (f["date"] <= d2)]

# KPIs
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Linhas", f"{len(f):,}")
kpi2.metric("Soma value", f"{f["value"].sum():,}")
kpi3.metric("Média value", f"{f["value"].mean():.2f}" if len(f) else "0")

# Gráfico interativo com Plotly
st.subheader("Evolução por data")
g = f.groupby("date", as_index=False)["value"].sum()

fig = px.line(
    g,
    x="date",
    y="value",
    markers=True,
    title="Soma de value por data"
)

fig.update_layout(
    xaxis_title="Data",
    yaxis_title="Value",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# Tabela
st.subheader("Dados filtrados")
st.dataframe(f, use_container_width=True)
