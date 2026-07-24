def post_something(username, cursor, connection):
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

def see_posts(cursor):
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

def search_post(cursor, connection):
        try:
            post_id = int(input("Enter the post id you want to search: "))
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

def delete_post(cursor, connection):
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

def edit_post(cursor, connection, user_id):
    try:
        edit_id = int(input("enter post_id you want to edit: "))
        
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
        
        if cursor.rowcount > 0:
            print("✅ Your post has been updated successfully.")
        else: 
            print("Post not found or you are not authorzed to edit it.")
    except ValueError:
        print("please enter valid pos id. ")