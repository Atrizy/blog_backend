import mariadb as db
import dbinteractions as dbi
import secrets
import hashlib

## This function is creaeting a login that will house all the user information.
def create_login_token():
    return secrets.token_urlsafe(70)

## This function gets all the users.
def get_users():
    success = False
    ## This empty array will be filled with what is returned from the database in the select statement below
    users = []
    ## This is what is needed to actually connect to the database
    conn, cursor = dbi.connect_db()
    try:
        ## This select statement is making a request to get all of the user that haev a blogger "status" and showing them to regular users and bloggers
        cursor.execute("SELECT id, username, email, pfp, profile_banner, bio, dob FROM users WHERE is_blogger=1")
        ## This fetchall statement is getting all the users and actually putting what it grab into the empty users ("users = []") array
        users = cursor.fetchall()
        ## Once everything is done the success will return as true 
        success = True
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success, users

## This is the code that will be called when logging in a user
def login_user(email, password):
    success = False
    id = None
    ## This is what is needed to actually connect to the database
    conn, cursor = dbi.connect_db()
    ## This is getting the user inputed email from the users table and comparing it to the salt that is in the db if they are both a match you will move onto the next step
    cursor.execute("SELECT salt FROM users WHERE email=?", [email])
    ## You only need to fetch one because with user input on the email the api only needs to compare one email to the salt
    salt = cursor.fetchone()
    ## This is the code thatis executing the 
    login_token = create_login_token()
    password = salt[0] + password
    password = hashlib.sha512(password.encode()).hexdigest()
    cursor.execute("SELECT id, email, username, bio, dob, pfp, profile_banner FROM users WHERE email=? AND password=?" [email, password])
    user = cursor.fetchone()
    try:
        if(cursor.rowcount == 1):
            cursor.execute("INSERT INTO user_session(user_id, login_token) VALUES(?,?)", [user[0], login_token])
            success = True
            id = cursor.lastrowid
    except db.ProgrammingError:
        print("There is an error with the SQL")
    except db.OperationalError:
        print("There was an issue with the DB")
    except:
        print("Something went wrong")
    dbi.disconnect_db(conn, cursor)
    return success, id, user, login_token, email

## This is for deleting a user, you need a valid login token to prove you are the owner of the account.
def delete_user(login_token):
    success = False
    conn, cursor = dbi.connect_db()
    try:
        cursor.execute("SELECT user_id FROM user_session WHERE login_token=?", [login_token])
        user = cursor.fetchone()
        cursor.execute("DELETE FROM users WHERE id=?", [user[0]] )
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