from dependencies import *

connection = sqlite3.connect("./Data/database.db", check_same_thread=False)
cursor = connection.cursor()
print(KEY)
client = OpenAI()

def get_response(client,system_intruction,text):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_intruction},
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return completion.choices[0].message.content

def run_sql_query(cursor,connection,sql_query):
    cursor.execute(sql_query)
    connection.commit()
    
def show_all_entries():
    cursor.execute("SELECT * FROM quotations")
    rows = cursor.fetchall()

    if rows:
        st.subheader("Current Entries in Database:")

        df = pd.DataFrame(rows, columns=[
            "quotation_id", "vendor_name", "quotation_text", 
            "created_at", "item_description", "item_quantity", 
            "total_amount", "currency", "status"
        ])
        
        st.dataframe(df)

    else:
        st.write("No entries found in the database.")