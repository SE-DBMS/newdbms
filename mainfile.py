from flask import Flask, render_template
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['SECRET_KEY']='wasteaf'
app.config["MONGO_URI"] = "mongodb://localhost:27017/wastedatabase"
mongo = PyMongo(app)

@app.route('/')
def screen1():
    return render_template('openscreen.html')


@app.route('/adminlogin')
def screen2():
    return render_template('index.html')


@app.route('/stafflogin')
def screen3():
    return render_template('index.html')

@app.route('/adminpage')
def screen4():
    return render_template('adminpage.html')

@app.route('/contactus')
def screen5():
    return render_template('contactus.html')

@app.route('/aboutus')
def screen6():
    todisplay=mongo.db.cleaners.find();
    return render_template('aboutus.html',todisplay=todisplay)


if __name__ == '__main__':
    app.run(debug=True)
