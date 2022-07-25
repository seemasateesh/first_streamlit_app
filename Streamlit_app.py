import streamlit
streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍍 Pineapple Omega 3 & 🫐 Blueberries Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Egg  Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado.Avacado Toast')
streamlit.header('🍏 🍉  Build your own fruit smoothie 🍋  🍍 ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
