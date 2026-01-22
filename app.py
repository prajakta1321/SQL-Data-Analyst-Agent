
import streamlit as st   # streamlit library

# Import SQL generation and execution logic
from agents.sql_generator import generate_sql
from agents.sql_executor import execute_sql

# Streamlit App Configuration
st.set_page_config(page_title="Ask The SQL Agent",layout="wide")

st.title("Ask The AI SQL Data Analyst Agent")

# Text box for user to ask a natural language question
question = st.text_input("Ask a question about your data.")

# Main Action Button
if st.button("Generate SQL"):

    # Generate SQL from natural language question
    sql = generate_sql(question)

    # Display generated SQL query
    st.subheader("Generated SQL Query")
    st.code(sql, language="sql")

    # Execute the generated SQL query on the database
    df, error = execute_sql(sql)

    # Display query result OR error message
    if error:
        # Show SQL execution error in red
        st.error(f"SQL Error: {error}")

        # Helpful tip for the user
        st.info(
            "Tip: Try asking questions related to existing tables "
            "(customers, orders, products).")
    else:
        # Display query result as a table
        st.subheader("Query Result")
        st.dataframe(df)
