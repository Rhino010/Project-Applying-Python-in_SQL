def add_member(cursor, name, age, conn):
    # Query to insert data and create a new member
    query = "INSERT INTO  Members (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    conn.commit()

def update_member(cursor, new_age, member_id, conn):
    # Query to update the age of a member by their id
    query = "UPDATE Members SET age = %s WHERE member_id = %s"
    cursor.execute(query,(new_age, member_id))
    conn.commit()
    print("Member age updated successfully.")

def get_members_in_age_range(cursor, start_age, end_age):
    # query to search database for members between specific ages
    query = "SELECT member_id, name, age FROM Members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (start_age, end_age))
    print(f"Here are the members between ages {start_age} and {end_age}:\n")
    for member in cursor.fetchall():
        print(member)