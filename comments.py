import mariadb as db
import dbinteractions as dbi


def get_all_comments():
    success = False
    comments = []
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute(
            "SELECT users.id, users.username, comment.content, comment.created_at, comment.id FROM comment INNER JOIN users ON users.id = comment.user_id")
        comments = cursor.fetchall()
        success = True
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success, comments

## This function is creating a comment, whatever the user inputs in the frontend it will be created as a comment
def insert_comment(login_token, content):
    success = False
    id = None
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("INSERT INTO comment(user_id, content) VALUES(?,?)", [user[0], content])
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

## This is for editing comments dpending on what is input on the frontend 
def patch_comment_info(login_token, content, id):
    success = False
    conn, cursor = dbi.connect_db()
    cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
    user = cursor.fetchone()
    try:
        cursor.execute("UPDATE comment SET content=? WHERE id=? AND user_id=?", [content, id, user[0]])
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

## This function deletes a comment after confirming that the user trying to delete the comment is the owner of the comment
def delete_comment(login_token, id):
    success = False
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("DELETE FROM comment WHERE id=? AND user_id=?", [id, user[0]] )
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