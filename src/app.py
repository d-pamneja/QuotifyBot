from dependencies import *
from system_instructions import *
from utils import *

st.title("WhatsApp Chat to SQL Converter")

whatsapp_chat = st.text_area("Enter WhatsApp Chat:", height=300)

if st.button("Execute"):
    if whatsapp_chat:
        sql_query = get_response(client,system_intruction[0],whatsapp_chat)
        run_sql_query(cursor,connection,sql_query)
        st.success("Query executed successfully!")

        cursor.execute("SELECT * FROM quotations;")
        entries = cursor.fetchall()
        
        if entries:
            show_all_entries()
            
    else:
        st.error("Please enter a WhatsApp chat.")
        