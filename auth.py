def register(cursor, connection):
    print("\n======== User Registration ============")
    
    username = input("enter your username: ")
    email = input("Enter your email: ")
    fullname = input("Enter your full name: ")
    password = input("Enter your password: ")
    
    cursor.execute(
        "SELECT username FROM users WHERE username = %s",
        (username,)
    )
    if cursor.fetchone():
        print ("Username already exists! ")
        return None
    else:
        cursor.execute(
        '''
        INSERT INTO users (full_name, username, email, password)
        VALUES(%s, %s, %s, %s)
        
        ''',
        (fullname, username, email, password)
        
        )
        connection.commit()
        print("registration successfull!")
        return login(cursor)
def login(cursor):
    print("\n============ User Login ==============")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    cursor.execute(
        '''
        SELECT user_id, username
        FROM users
        WHERE username=%s AND password = %s
        
        ''',
        (username, password)
        
    )
    user = cursor.fetchone()
    
    if user:
        print("login successfully!")
        return {
            "user_id": user[0],
            "username": user[1]
        }
    else:
        print("invalid username or password.")
        return None