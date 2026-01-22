

from utils.schema import SCHEMA_INFO

def generate_sql(user_question: str):
    """
    Converts a natural language question into an SQL query.
    - This is a rule-based SQL generator.
    - It simulates how an LLM would convert user questions into SQL.
    - The logic can later be replaced by an actual LLM call.
    """

    # Convert user input to lowercase for easy matching
    question = user_question.lower()

    # If user asks for all users
    if "all users" in question or "all customers" in question:
        return "SELECT * FROM customers;"

    # If user asks for all orders
    if "all orders" in question:
        return "SELECT * FROM orders;"

    # If user asks for all products
    if "all products" in question:
        return "SELECT * FROM products;"

    # If user asks for count of users/customers
    if "count" in question and ("users" in question or "customers" in question):
        return "SELECT COUNT(*) FROM customers;"

    # Fallback if question is not understood
    return "Unable to generate SQL for this query"
