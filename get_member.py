from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #SQL query
        query = "SELECT * FROM Members"
        
        #Executing the query
        cursor.execute(query)

        #Fetching and displaying the results
        for member in cursor.fetchall():
            print(member)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()