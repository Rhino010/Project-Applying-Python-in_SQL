from member_funcs import add_member, update_member, get_members_in_age_range
from workout_funcs import add_workout, delete_workout
from connect_mysql import connect_database


def main():

    conn = connect_database()

    if conn is not None:
        cursor = conn.cursor()
        try:
            while True:
                # Options menu
                print(" ")
                print("***LOCAL GYM MEMBER SYSTEM***")
                print(" ")
                print("1. Add a Member")
                print("2. Add a Workout Session")
                print("3. Update Member Age")
                print("4. Delete Workout Session")
                print("5. Find Members By Age Range")
                print("6. Quit Program")
                choice = input("Please type option '1 - 5' and hit 'Enter'.\n")

                if choice == '1':
                    # Inputs for each data column
                    member_name = input("Please enter member's name:\n")
                    member_age = int(input("Please enter member's age:\n"))
                    # Function imported from add_member.py
                    add_member(cursor, member_name, member_age, conn)

                elif choice == '2':
                    # Inputs for each data column
                    member_id = int(input("Enter the member's ID:\n"))
                        
                    # Checking if member exists in the database.
                    check_for_member = "SELECT member_id FROM Members WHERE member_id = %s"
                    cursor.execute(check_for_member, (member_id, ))
                    member = cursor.fetchone()
                    # Checking if member is valid
                    if member:
                        session_date = input("Enter date as (YYYY-MM-DD):\n")
                        session_minutes = int(input("How many minutes was this session?\n"))
                        calories_burned = int(input("How many calories were burned in this session?\n"))
                        # Function imported from add_workout.py
                        add_workout(cursor, member_id, session_date, session_minutes, calories_burned, conn)
                        print("Session information added successfully.")
                    else:
                        print("That member does not exist. Please try again.")

                elif choice == '3':
                    member_id = int(input("Please enter the member's ID:\n"))
    
                    # Checking if member exists in the database.
                    check_for_member = "SELECT member_id FROM Members WHERE member_id = %s"
                    cursor.execute(check_for_member, (member_id, ))
                    member = cursor.fetchone()
                    # Checking if member is valid
                    if member:
                        new_age = int(input("Please enter the new age of the member:\n"))
                        update_member(cursor, new_age, member_id, conn)
                    else:
                        print(f"No member found with ID: {member_id}")

                elif choice == '4':
                    session_id = int(input("Enter the workout session ID:\n"))
                    # Searching database for user input session_id
                    check_for_session = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s"
                    cursor.execute(check_for_session, (session_id, ))
                    session = cursor.fetchone()
                    # Checking if the session_id is valid
                    if session:
                        member_id = int(input("Enter the member's ID:"))
                        # Searching database for user input member_id
                        check_for_member = "SELECT member_id FROM Members WHERE member_id = %s"
                        cursor.execute(check_for_member, (member_id, ))
                        member = cursor.fetchone()
                        # Checking if member_id is valid
                        if member:
                            delete_workout(cursor, session_id, member_id, conn)
                            print("Workout deleted successfully.")
                        else:
                            print("That member does not exist. Please try again.")
                    else:
                        print("That session does not exist. Please try again.")

                elif choice == '5':
                    start_age = int(input("Please type the lowest age you wish to start with.\n"))
                    end_age = int(input("Please type the highest age you would like to search to.\n"))
                    # Checking to make sure they start with the lowest age first.
                    if end_age < start_age:
                        print("Please start with the lowest age of the range you wish to search.")
                    else:
                        get_members_in_age_range(cursor, start_age, end_age)
                
                elif choice == '6':
                    print("Closing program.....")
                    break
                    

        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
        
# TODO: look for areas to add checks and make sure members and sessions align or any other checks that may need to be done.
