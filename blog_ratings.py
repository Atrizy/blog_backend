import mariadb as db
import dbinteractions as dbi

def rate_blog(login_token, blog_id):
    success = False
    id = None
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("INSERT INTO blog_rating(user_id, blog_id) VALUES(?,?)", [user[0], blog_id])
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
    likes = []
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT users.username, blog_rating.blog_id, blog_rating.user_id FROM users INNER JOIN blog_rating ON blog_rating.user_id = users.id WHERE blog_rating.blog_id=?", [blog_id])
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
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("DELETE FROM blog_rating WHERE id=? AND user_id=? AND blog_id=?", [id, user[0], blog_id] )
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