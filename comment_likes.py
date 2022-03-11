import mariadb as db
import dbinteractions as dbi

def comment_like(login_token, comment_id):
    success = False
    id = None
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("INSERT INTO comment_like(user_id, comment_id) VALUES(?,?)", [user[0], comment_id])
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

def get_comment_like(comment_id):
    success = False
    likes = []
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT users.username, comment_like.comment_id, comment_like.user_id FROM users INNER JOIN comment_like ON comment_like.user_id = users.id WHERE comment_like.comment_id=?", [comment_id])
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

def delete_comment_like(login_token, id, comment_id):
    success = False
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("DELETE FROM comment_like WHERE id=? AND user_id=? AND comment_id=?", [id, user[0], comment_id] )
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