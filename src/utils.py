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