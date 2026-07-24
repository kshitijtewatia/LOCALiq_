def view_comment(cursor):
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

def add_comment(cursor, connection, username):
        p_id = int(input("enter post id which you want to comment: "))
        u_name = username
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