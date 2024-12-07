

def add_workout(cursor, member_id, session_date, session_minutes, calories_burned, conn):
    query = "INSERT INTO  WorkoutSessions (member_id, session_date, session_minutes, burned_calories) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (member_id, session_date, session_minutes, calories_burned))
    conn.commit()


def delete_workout(cursor, session_id, member_id, conn):
    query = "DELETE FROM WorkoutSessions WHERE session_id = %s AND member_id = %s"
    cursor.execute(query, (session_id, member_id))
    conn.commit()
    print("Workout session has been deleted successfully.")