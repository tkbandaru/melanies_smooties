# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

helpful_links = [
    "https://docs.streamlit.io",
    "https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit",
    "https://github.com/Snowflake-Labs/snowflake-demo-streamlit",
    "https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake"
]

st.title('Customize your SMOOTHIE!')
st.write('Choose the fruits you want in your custom Smoothie')

#option = st.selectbox ( 'What is your favorite fruit?',
#                       ('Banana', 'Strawberries', 'Peaches'))

#st.write('your favorite fruit is : ', option)

name_on_order = st.text_input('name on smoothie')
#st.write(name_on_order)

session = get_active_session()
my_df = session.table("SMOOTHIES.PUBLIC.FRUIT_OPTIONS").select(col('FRUIT_NAME'))
#st.dataframe(data = my_df, use_container_width=True)

ingredients_list = st.multiselect('choose upto 5 ingredients :', my_df, max_selections=5)

if ingredients_list :
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string = ''
    for i in ingredients_list:
        ingredients_string = ingredients_string + i
    #st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
    values ('""" + ingredients_string + """','""" +name_on_order+"""')"""
    
    #st.write(my_insert_stmt)
    time_insert = st.button('submit order')
    if time_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered! '+name_on_order, icon="✅")











