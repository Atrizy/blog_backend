import mariadb as db
import dbinteractions as dbi

## This function is inserting the posts depending on the user input
def insert_post(login_token, content):
    success = False
    id = None
    ## Connecting to the db
    conn, cursor = dbi.connect_db()
    try:
        ## Getting the login token to figure out which user is trying to make a post 
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        ## Depending on what the user is inputting this INSERT statement will insert the users id and the content that is provided on the front end 
        cursor.execute("INSERT INTO blog_post(user_id, content) VALUES(?,?)", [user[0], content])
        ## This is commiting the changes to the database
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

def get_all_posts():
    success = False
    ## This empty array will be filled with what is returned from the database in the select statement below
    posts = []
    ## Connecting to the db
    conn, cursor = dbi.connect_db()
    try:
        ## This select statement is grabbing all the bloggers posts and joining the the users table to get the bloggers user id
        cursor.execute(
            "SELECT users.username, blog_post.content, blog_post.created_at, blog_post.id from users INNER JOIN blog_post ON users.id = blog_post.user_id")
        ## This fetchall statement is getting all the posts and actually putting what it grab into the empty posts ("posts = []") array
        posts = cursor.fetchall()
        success = True
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success, posts

def patch_blog_post_info(login_token, content, id):
    success = False
    ## Connecting to the db
    conn, cursor = dbi.connect_db()
    ## This is grabbing your login token to make sure that you the owner of the blog post before the function can actually work
    cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
    ## This fetchone statement is getting the everything about the user
    user = cursor.fetchone()
    try:
        ## This cursor.execute statement is updating the information on the backend through the db and taking in input from the frontend through the user to update their blog posting
        cursor.execute("UPDATE blog_post SET content=? WHERE id=? AND user_id=?", [content, id, user[0]])
        ## Commiting the changes above
        conn.commit()
        success = True       
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success

def delete_blog_post(login_token, id):
    success = False
    ## Connecting to the db
    conn, cursor = dbi.connect_db()
    try:
         ## This is grabbing your login token to make sure that you the owner of the blog post before the function can actually delete the posting
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        ## This is deleting the post from the db
        cursor.execute("DELETE FROM blog_post WHERE id=? AND user_id=?", [id, user[0]] )
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