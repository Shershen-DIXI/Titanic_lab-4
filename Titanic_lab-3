import streamlit as st
import pandas as pd

st.image("titanic.jpg")

st.title("Пассажиры Титаника")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('titanic_train.csv')
        return df
    except FileNotFoundError:
        st.error("Файл 'titanic_train.csv' не найден")
        return None

df = load_data()

if df is not None:
    st.sidebar.header("Фильтры")
    
    # Фильтр только для женщин
    filtered_df = df[df['Sex'] == 'female']
    
    # Фильтр только для выживших
    filtered_df = filtered_df[filtered_df['Survived'] == 1]
    
    class_filter = st.sidebar.multiselect(
        "Класс:",
        options=sorted(filtered_df['Pclass'].unique()),
        default=sorted(filtered_df['Pclass'].unique())
    )
    
    # Ползунок платы за проезд
    fare_range = st.sidebar.slider(
        "Плата за проезд:",
        min_value=float(filtered_df['Fare'].min()),
        max_value=float(filtered_df['Fare'].max()),
        value=(float(filtered_df['Fare'].min()), float(filtered_df['Fare'].max()))
    )
    
    filtered_df = filtered_df[filtered_df['Pclass'].isin(class_filter)]
    filtered_df = filtered_df[(filtered_df['Fare'] >= fare_range[0]) & (filtered_df['Fare'] <= fare_range[1])]
    
    st.dataframe(filtered_df, use_container_width=True)
    st.write(f"Найдено записей: {len(filtered_df)}")
