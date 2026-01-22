import sqlite3
import pandas as pd

def execute_sql(sql_query):    # Executes a given SQL query on the SQLite database.
    conn = sqlite3.connect("db/sales.db")   # Connect to the SQLite database. The database file is stored inside the db/ folder

    try:
        df = pd.read_sql_query(sql_query, conn)    # sql_query (str): SQL query generated from user input
        conn.close()                               # Execute SQL query and store result in a DataFrame
        return df, None                            # Return result and no error
    except Exception as e:
        conn.close()                               # Close the connection even if an error occurs
        return None, str(e)                        # Return no data and the error message
