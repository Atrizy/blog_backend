import post as po
import signup as su
import login as log
import comments as cm
import comment_likes as cl
import blog_ratings as br
from flask import Flask, request, Response
import json
import dbinteractions as db
import sys

app = Flask(__name__)

# Beginning of the GET, POST, PATCH and DELETE, this is what the backend will be interacting with everything regarding posts and post ratings
@app.get("/api/blog_likes")
def get_blog_likes():
    try:
        blog_id = request.args["blog_id"]
        success, post = br.get_blog_rating(blog_id)
        if(success):
            blog_rating_json = json.dumps(post, default=str)
            return Response(blog_rating_json, mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.get("/api/post")
def get_blog_post():
    try:
        success, post = po.get_all_posts()
        if(success):
            posts_json = json.dumps(post, default=str)
            return Response(posts_json, mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.post("/api/post")
def insert_post():
    try:
        login_token = request.json['login_token']
        content = request.json['content']
        success, id = po.insert_post(login_token, content)
        if(success):
            post_json = json.dumps({
                "login_token":login_token,
                "content": content,
                "id": id
            }, default=str)
            return Response(post_json, mimetype="application/json", status=201)
        else:
            return Response("Invalid post", mimetype="plain/text", status=400)
    except KeyError:
        return Response("Invalid username or content", mimetype="plain/text", status=422)
    except:
        return Response("Please try again later", mimetype="plain/text", status=501)

@app.post("/api/blog_likes")
def like_blog():
    try:
        login_token = request.json["login_token"]
        blog_id = request.json["blog_id"]
        success = br.rate_blog(login_token, blog_id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.patch("/api/post")
def patch_blog_information():
    try:
        id = request.json["id"]
        content = request.json["content"]
        login_token = request.json["login_token"]
        success = po.patch_blog_post_info(login_token, content, id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.delete("/api/post")
def delete_blog_post():
    try:
        login_token = request.json["login_token"]
        id = request.json["id"]
        success = po.delete_blog_post(login_token, id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.delete("/api/blog_likes")
def delete_blog_like():
    try:
        login_token = request.json["login_token"]
        id = request.json["id"]
        blog_id = request.json["blog_id"]
        success = br.delete_blog_rating(login_token, id, blog_id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)
## Ending of the GET, POST, PATCH and DELETE, this is what the backend will be interacting with everything regarding posts and post ratings

## Beginning of the GET, POST, PATCH and DELETE, this is what the backend will be interacting with everything regarding the users
@app.get("/api/users")
def get_bloggers():
    try:
        success, users = log.get_users()
        if(success):
            users_json = json.dumps(users, default=str)
            return Response(users_json, mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Something went horribly wrong please call someone", mimetype="plain/text", status=500)

@app.post("/api/users")
def create_user():
    try:
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']
        bio = request.json['bio']
        dob = request.json['dob']
        pfp = request.json.get('pfp')
        profile_banner = request.json.get("profile_banner")
        success, id, login_token = su.signup(email, username, password, bio, dob, pfp, profile_banner)
        if(success):
            user_json = json.dumps({
                "user_id": id,
                "email": email,
                "username": username,
                "bio": bio,
                "dob": dob,
                "pfp": pfp,
                "profile_banner": profile_banner,
                "login_token": login_token
            })
            return Response(user_json, mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Something went horribly wrong please call someone", mimetype="plain/text", status=500)

@app.patch("/api/users")
def patch_user_profile():
    try:
        email = request.json['email']
        username = request.json['username']
        bio = request.json['bio']
        dob = request.json['dob']
        pfp = request.json.get('pfp')
        profile_banner = request.json.get("profile_banner")
        login_token = request.json["login_token"]
        success = su.patch_user_info(login_token, email, username, bio, dob, pfp, profile_banner)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.delete("/api/users")
def delete_user():
    try:
        login_token = request.json["login_token"]
        success = log.delete_user(login_token)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)
## Ending of the GET, POST, PATCH and DELETE, this is what the backend will be interacting with everything regarding the users

## Beginning of the GET, POST, PATCH and DELETE, this is what the backend will be interacting with everything regarding the comments and comment likes
@app.get("/api/comment_likes")
def get_comments_likes():
    try:
        comment_id = request.args["comment_id"]
        success, post = cl.get_comment_like(comment_id)
        if(success):
            comment_likes_json = json.dumps(post, default=str)
            return Response(comment_likes_json, mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.get("/api/comments")
def get_blog_comments():
    try:
        success, post = cm.get_all_comments()
        if(success):
            comments_json = json.dumps(post, default=str)
            return Response(comments_json, mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.post("/api/comments")
def insert_comment():
    try:
        login_token = request.json['login_token']
        content = request.json['content']
        success, id = cm.insert_comment(login_token, content)
        if(success):
            comment_json = json.dumps({
                "login_token":login_token,
                "content": content,
                "id": id
            }, default=str)
            return Response(comment_json, mimetype="application/json", status=201)
        else:
            return Response("Invalid comment format", mimetype="plain/text", status=400)
    except KeyError:
        return Response("Invalid username or content", mimetype="plain/text", status=422)
    except:
        return Response("Please try again later", mimetype="plain/text", status=501)

@app.post("/api/comment_likes")
def like_comment():
    try:
        login_token = request.json["login_token"]
        comment_id = request.json["comment_id"]
        success = cl.comment_like(login_token, comment_id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.patch("/api/comments")
def patch_comment_information():
    try:
        id = request.json["id"]
        content = request.json["content"]
        login_token = request.json["login_token"]
        success = cm.patch_comment_info(login_token, content, id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.delete("/api/comments")
def delete_comment():
    try:
        login_token = request.json["login_token"]
        id = request.json["id"]
        success = cm.delete_comment(login_token, id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)

@app.delete("/api/comment_likes")
def delete_comment_like():
    try:
        login_token = request.json["login_token"]
        id = request.json["id"]
        comment_id = request.json["comment_id"]
        success = cl.delete_comment_like(login_token, id, comment_id)
        if(success):
            return Response(mimetype="application/json", status=200)
        else:
            return Response("Please try again", mimetype="plain/text", status=400)
    except:
        return Response("Sorry Please try again", mimetype="plain/text", status=500)
## Ending of the GET, POST, PATCH and DELETE, this is what the backend will be interacting with everything regarding the comments and the comment likes

if(len(sys.argv) > 1):
    mode = sys.argv[1]
else:
    print("You must pass a mode to run this python script, either 'testing' or 'production'")
    exit()

if(mode == "testing"):
    print("Running in testing mode")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif(mode =="production"):
    print("Running in production mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("Please run with either testing or production. Example: ")
    print("python app.py production")