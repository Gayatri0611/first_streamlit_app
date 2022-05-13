
import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and blueberry oatmeal')
streamlit.text('Pav bhaji')

streamlit.title('build your own fruit smoothieee')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include streamlit.multiselect("Pick some fruits:", list (my fruit_list.index))
streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index))
#Edisplay the table on the page
streamlit.dataframe (my_fruit_list)

#Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])

#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

