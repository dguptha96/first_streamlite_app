import streamlit
import pandas

streamlit.title("My parents new healthy diner")

streamlit.header("Breakfast Menu")

streamlit.text("omega 3 & Blueburry oatmeal")

streamlit.text("kela, Spinach & Rocket Smootie")

streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
