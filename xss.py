from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/search')
def get_query():
    query = request.args.get("query")
    if query:
        return 'I see that you are looking for: ' + query
    else:
        return 'What are you looking for? Ask me a question.'
 
@app.route('/comments/add', methods = ['POST'])
def get_comment():
   comment = request.form["comment"]
   if comment:
        with open("comments.txt", "a") as comment_file:
            comment_file.write(comment + "\n")
        return "Successfully added comments"
   else:
        return "No comments received"

@app.route('/comments')
def comments_list():
    comments = ""
    with open("comments.txt") as comment_file:
        ctr = 1
        line = comment_file.readline()       
        while line:
            comments += ("Comment " + str(ctr) + ": " + line + "<br>")
            line = comment_file.readline()
            ctr += 1
    comments += '''
        <hr>
        <form action="/comments/add" method = "POST">
        Enter a Comment: <br>
        <input type="text" name="comment">
        <input type="submit" value="Submit">
        </form> 
    '''
    return comments
 
