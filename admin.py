from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)
@app.route('/books')
def book():
    books=[{'name':'book1','author':'abc','cover':'https://edit.org/images/cat/book-covers-big-2019101610.jpg'}, {'name':'book2','author':'xyz','cover':'https://edit.org/images/cat/book-covers-big-2019101610.jpg'},
           {'name':'book3','author':'mno','cover':'https://edit.org/images/cat/book-covers-big-2019101610.jpg'}]
    return render_template('book.html',books=books)

app.run(debug=True)