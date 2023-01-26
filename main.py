import sqlite3
import streamlit as st
import pandas as pd
import os


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        st.write(e)

    return conn


def run_query():
    st.markdown("# Run Query")
    db_filename = "weather.db"

    query = st.text_area("SQL Query", height=100)
    conn = create_connection(db_filename)

    submitted = st.button("Run Query")

    if submitted:
        try:
            query = conn.execute(query)
            cols = [column[0] for column in query.description]
            results_df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
            st.dataframe(results_df)
        except Exception as e:
            st.write(e)

    st.sidebar.markdown("# Run Query")


page_names_to_funcs = {
    "Run Query": run_query,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
