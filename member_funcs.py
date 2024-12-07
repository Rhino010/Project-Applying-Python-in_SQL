def add_member(cursor, name, age, conn):
    query = "INSERT INTO  Members (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    conn.commit()

def update_member(cursor, new_age, member_id, conn):
    query = "UPDATE Members SET age = %s WHERE member_id = %s"
    cursor.execute(query,(new_age, member_id))
    conn.commit()
    print("Member age updated successfully.")

def get_members_in_age_range(cursor, start_age, end_age):
    query = "SELECT member_id, name, age FROM Members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (start_age, end_age))
    print(f"Here are the members between ages {start_age} and {end_age}:\n")
    for member in cursor.fetchall():
        print(member)