import os
import streamlit as st
import pandas as pd

from src.db_ops import show_data, edit_data, delete_data

def parameter_insertion(cursor, db):
    st.header('💸 Parameter Insertion')
    # st.write(st.session_state)
    if 'flag' not in st.session_state:
        st.session_state.flag = 0
    with st.form(key='expense_submit_form', clear_on_submit=False, border=True):
        datatype_catagory = ['Numbers', 'Text', 'Sequence', 'Others']
        purpose = st.text_area('Purpose')
        datatype = st.selectbox('Datatype*', datatype_catagory)
        created_at = st.date_input('Expense Date*')
        updated_at = st.date_input('Updated at*')
        if st.form_submit_button(label='Submit'):
            if not(created_at and datatype and purpose):
                st.error('Please fill all the * fields')
            else:
                st.session_state.flag = 1
                # st.success('Data Submitted Successfully')
    if st.session_state.flag:
        # st.write(final_parameter_calculation)

        with st.form(key='final', clear_on_submit=True, border=True):
             # st.write(final_parameter_calculation)

            if st.form_submit_button('Are you Sure?'):
                # st.write(final_parameter_calculation)
                # insert data into expense table
                query = '''Insert into parameter (purpose, datatype, created_at, 
                                                updated_at) 
                        VALUES (%s, %s, %s, %s)
                        '''
                values = (purpose, datatype, created_at, updated_at)
                # st.write(query, values)
                cursor.execute(query, values)
                db.commit()
                st.success("Parameter Inserted Successfully!")
                st.balloons()

            else:
                st.write("Click above button If you are Sure")
    else:
        st.warning("Please fill up above form")

    #df = pd.read_sql('''SELECT purpose, datatype, created_at, updated_at''', con=db)
    