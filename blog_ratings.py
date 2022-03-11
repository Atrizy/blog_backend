import mariadb as db
import dbinteractions as dbi

## This functoin is adding a like to a blog
def rate_blog(login_token, blog_id):
    success = False
    id = None
    ## Connecting to the db
    conn, cursor = dbi.connect_db()
    try:
        ## Getting the login token to figure out which user is trying to make like a blog post
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        ## This fetchone statement is getting the everything about the user
        user = cursor.fetchone()
        ## This is inserting the like onto the blog post
        cursor.execute("INSERT INTO blog_rating(user_id, blog_id) VALUES(?,?)", [user[0], blog_id])
        ## Commiting the changes
        conn.commit()
        if(cursor.rowcount == 1):
            success = True
            id = cursor.lastrowid
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success, id

def get_blog_rating(blog_id):
    success = False
    ## This empty array will be filled with what is returned from the database in the select statement below
    likes = []
    ## Connecting to the db
    conn, cursor = dbi.connect_db()
    try:
        ## This select statement is grabbing all the blog likes and joining the the users table so that the backend can figure out what user is liking the blog
        cursor.execute("SELECT users.username, blog_rating.blog_id, blog_rating.user_id FROM users INNER JOIN blog_rating ON blog_rating.user_id = users.id WHERE blog_rating.blog_id=?", [blog_id])
        ## This is fetching all the comments and inputting into the empty likes ("likes = []") array
        likes = cursor.fetchall()
        success = True
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success, likes

def delete_blog_rating(login_token, id, blog_id):
    success = False
    conn, cursor = dbi.connect_db()
    try:
        ## Getting the login token to figure out which user is trying to make like a blog post
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        ## This fetchone statement is getting the everything about the user
        user = cursor.fetchone()
        ## This execute statement is removing the like from the blog posting depending on the users id
        cursor.execute("DELETE FROM blog_rating WHERE id=? AND user_id=? AND blog_id=?", [id, user[0], blog_id])
        ## Commiting the changes
        conn.commit()
        if(cursor.rowcount == 1):
            success = True
            id = cursor.lastrowid
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success