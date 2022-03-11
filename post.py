import mariadb as db
import dbinteractions as dbi

def insert_post(login_token, content):
    success = False
    id = None
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("INSERT INTO blog_post(user_id, content) VALUES(?,?)", [user[0], content])
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
    posts = []
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute(
            "select users.username, blog_post.content, blog_post.created_at, blog_post.id from users inner join blog_post on users.id = blog_post.user_id")
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
    conn, cursor = dbi.connect_db()
    cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
    user = cursor.fetchone()
    try:
        cursor.execute("UPDATE blog_post SET content=? WHERE id=? AND user_id=?", [content, id, user[0]])
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
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
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