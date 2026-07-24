from database import get_connection
from auth import login, register
from posts import post_something, see_posts, search_post, delete_post, edit_post
from comments import view_comment, add_comment
connection = get_connection()
cursor = connection.cursor()
#######################create table########################

print("1. Login")
print("2. Register")

userc = int(input("enter your choice: "))

if userc == 1:
    current_user = login(cursor)
    
elif userc == 2:
    current_user = register(cursor, connection)
else:
    print("invalid choice")
    exit()
if current_user is None:
    exit()
username = current_user["username"]
user_id = current_user["user_id"]
run = True




while run==True:
    print("""
===============================================================
                    LOCAL IQ
              Community Update System
===============================================================

               ===== MAIN MENU =====

  [1] Post Something
  [2] View All Posts
  [3] Exit Application
  [4] Search Post by ID
  [5] Delete Post by ID
  [6] Edit Post by ID
  [7] Add comment
  [8] view comment

===============================================================
Choose an option:
""")
    
    try:
        choice=int(input("enter your choice please: "))
    except ValueError:
        print("please enter valid number.............")
        continue
    if choice==1:
        post_something(username, cursor, connection)
        
        
    elif choice==2:
        see_posts(cursor)
        
            
    elif choice == 3:
        print("""
====================================
     See you again on LOCAL IQ! 🌍
        Goodbye and take care!
====================================
""")
        break
    
    elif choice == 4:
        search_post(cursor, connection)
        
    elif choice == 5:
        delete_post(cursor, connection)
    elif choice == 6:
        edit_post(cursor, connection, user_id)
    
    elif choice == 7:
        add_comment(cursor, connection, username)
    
    elif choice == 8:
        view_comment(cursor)
    else:
        print("please enter valid number: ")

cursor.close()
connection.close()
