import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("pokemon_dataset.csv")

st.write("# MY FIRST APP IN STREAMLIT")

df
st.write(df.describe())

st.write(df.isna().sum())



st.write(df.groupby("type_01")["name"].count())

# tab1, tab2, tab3 = st.tabs(["", "Kuchuk", "Boyo'gli (Boyqush)"])


# st.line_chart(df["type_01"])
# bin = st.select_slider(
#     "select bin number",
#     options=list(range(1, 26)))

# st.write("My favorite color is", bin)


fig, ax = plt.subplots()
sns.histplot(df['type_01'], bins=bin, ax=ax)
plt.xticks(rotation=90)

st.pyplot(fig)

genre = st.radio(
    label = "Tajriba Darajasini Tanlang",
    options = df['type_01'].unique().tolist(),
    index=None,
)

if st.button("Jadvalni Ko'rsat"):
    # st.write("Why hello there")
    st.write("You selected:", genre)

    st.dataframe(df[df["type_01"]==genre])
else:
    pass



with st.sidebar:

    st.line_chart(df["type_01"])

    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

tab1, tab2, tab3,tab4, tab5, tab6 = st.tabs(["Bulbasaur", "Hypno", "Charmander","Squirtle","Caterpie","Nidoran"])

with tab1:
   st.header("Bulbasaur")
   st.image("https://i.pinimg.com/736x/45/9c/22/459c2265febad6cff5349a9e7863d1b6.jpg", width=200)

  #  st.line_chart(df["Salary_USD"])

with tab2:
   st.header("A dog")
   st.image("https://i.ytimg.com/vi/4ytI2fUdVQc/maxresdefault.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://prixoxo.ru/uploads/posts/2023-10/prixoxo.ru_krasivye-risunki-charmander-69.png", width=200)

with tab4:
   st.header("A cat")
   st.image("https://i.pinimg.com/originals/09/49/d5/0949d53b1309c1e1573e2c20239cbe33.jpg", width=200)

  #  st.line_chart(df["Salary_USD"])

with tab5:
   st.header("A dog")
   st.image("https://i.pinimg.com/originals/dd/cb/b4/ddcbb4b0668811263d209de8fde763f5.png", width=200)

with tab6:
   st.header("An owl")
   st.image("https://i.gifer.com/8Xlz.gif", width=200)
