import streamlit as st
import pandas as pd

personnel = pd.read_csv("russia_losses_personnel.csv")
equipment = pd.read_csv("russia_losses_equipment.csv")

war = pd.merge(equipment, personnel, on=["date", "day"])
war["equipment_loss"] = war['aircraft'] + war['helicopter'] + war['tank'] + war['APC'] + war['field artillery'] + war['naval ship']


st.set_page_config(
    page_title="Russia-Ukraine war dashboard",
    page_icon="✅",
    layout="wide",
)

# dashboard title
st.title("Russia-Ukraine War")

st.header("Database overview")
st.dataframe(war)

