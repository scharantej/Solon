 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    return render_template('lesson.html', lesson_id=lesson_id)

@app.route('/quiz/<int:lesson_id>')
def quiz(lesson_id):
    return render_template('quiz.html', lesson_id=lesson_id)

@app.route('/forum')
def forum():
    return render_template('forum.html')

if __name__ == '__main__':
    app.run(debug=True)
