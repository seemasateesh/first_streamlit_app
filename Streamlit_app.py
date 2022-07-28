import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍍 Pineapple Omega 3 & 🫐 Blueberries Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Egg  Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado.Avacado Toast')
streamlit.header('🍏 🍉  Build your own fruit smoothie 🍋  🍍 ')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))

#fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
streamlit.error ('Please select a fruit to get information')

else :
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Copy the Jsonformat response to normalize 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Creating dataframe for fruityvice_normalized
streamlit.dataframe(fruityvice_normalized)

except URLError as e:
    streamlit.error()

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_row)


my_cur.execute(" insert into fruit_load_list values  ('from streamlit') ")
#my_cnx.commit()

# Allow end user to add a fruit to the list
streamlit.header("Fruityvice Fruit Advice!")
add_my_fruit = streamlit.text_input('What fruit would you like to add ?', 'jackfruit')
streamlit.write('Thanks for adding ' ,add_my_fruit )


  
#print(my_cur.rowcount, "details inserted")
  
# disconnecting from server
#my_cnx.close()
