from database import get_connection
from auth import login, register
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
    if choice==1:
        user_name = username
        category = input("Enter your category: ")
        city = input("enter your city name: ")
        message=input("What's new about the city: ")
        ############ QUERY TO SEND TO SQL###################
        query = '''
        INSERT INTO posts
        (user_name, category, city, message) 
        VALUES(%s, %s, %s, %s)
        
        '''
        ############ SENDING VALUES WITH QUERY ###############
        values = (
            user_name,
            category,
            city,
            message
        )
        ##################### SENDING TO STORE ##################
        cursor.execute(query, values)
        connection.commit()
        
        print("posted successfully.......")
    elif choice==2:
        ################ SELECTING ALL DATA FROM TABLE#########################
        cursor.execute(
            "SELECT * FROM posts ORDER BY created_at DESC"
        )
        #################### fETCHING DATA TO SHOW TO USERS ################################
        posts = cursor.fetchall()
        
        print("--------------- latest updates -------------")
        for post in posts:
            print("\nPost ID:", post[0])
            print("User:", post[1])
            print("Category:", post[2])
            print("City:", post[3])
            print("Update:", post[4])
            print("Time:", post[5])
            
    elif choice == 3:
        print("""
====================================
     See you again on LOCAL IQ! 🌍
        Goodbye and take care!
====================================
""")
        break
    
    elif choice == 4:
        try:
            post_id = int(input("Enter the post id you want to delete: "))
        except ValueError:
            print("enter valid value please...........")
        cursor.execute(
            '''SELECT * FROM posts
            where post_id = %s;
            ''',
            (post_id,)
        )
        result = cursor.fetchone()
        if result:
            print("congrats we found your post hurray.............")
            print(result)
        else:
            print("result not found........")
    
    elif choice == 5:
        try:
            delete_post = int(input("Enter the post id number you want to delete: "))
        except ValueError:
            print("please enter valid number...................")
        cursor.execute(
            '''
            DELETE FROM posts
            WHERE post_id = %s
            ''',
            (delete_post,)
            
        )
        connection.commit()
        print("post is deleted please check by press 2 on main menu>>>>>>>>")
    elif choice == 6:
        try:
            edit_id = int(input("enter the post id you want to edit: "))
        except ValueError:
            print("enter valid input: ")
            continue
        mess_age= input("enter what you want to write: ")
        
        cursor.execute(
            
            '''
            UPDATE posts
            SET message = %s
            WHERE post_id = %s
            ''',
            (mess_age, edit_id,)
            
        )
        connection.commit()
        print("your post is now updated ....>>>>>>>>")
    
    elif choice == 7:
        p_id = int(input("enter post id which you want to comment: "))
        u_name = input("enter your username: ")
        cmnt = input("enter your comment: ")
        cursor.execute(
            '''
            INSERT INTO comments
            (post_id, user_name, comment)
            VALUES(%s, %s, %s)
            
            ''',
            (p_id, u_name, cmnt)
            
        )
        connection.commit()
        print("your comments is added <<<<<<<<<<<<>>>>>>>>>")
    
    elif choice == 8:
        p_id = int(input("enter your post id you want to view comment: "))
        cursor.execute(
            '''
            SELECT * FROM comments
            WHERE post_id = %s
            ORDER BY created_at ASC
            ''',
            (p_id,)
            
        )
        comments = cursor.fetchall()
        if comments:
            print("\n------------- comments ------------")
            for comment in comments:
                print("user: ", comment[2])
                print("comment: ", comment[3])
                print("Time:", comment[4])
                print("-" *30)
        else:
            print("no comments found for this post...")
        
    else:
        print("please enter valid number: ")

cursor.close()
connection.close()
