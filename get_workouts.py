from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #SQL query
        query = "SELECT * FROM workoutsessions"
        
        #Executing the query
        cursor.execute(query)

        #Fetching and displaying the results
        for workout in cursor.fetchall():
            print(workout)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()