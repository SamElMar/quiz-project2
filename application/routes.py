from application import app, db
from application.models import *
from flask import request, redirect, url_for, render_template
from application.forms import *
from application.forms import *
# Might need to go back to Templates - Expressions/statements video

@app.route('/', methods = ['GET', 'POST'])
def Login_page():
    form = LoginForm()
    if form.validate_on_submit():
        forname = form.forname.data
        surname = form.surname.data
        username = form.username.data
        new_user = Login(username = username, forename = forname, surname = surname) 
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('create_questions_options_answers'))
    return render_template('login.html', form = form)

# Create
@app.route('/create_questions_options_answers', methods = ['GET', 'POST'])
def create_questions_options_answers():
    form = create_questions_options_answersForm()
    if request.method == 'POST':
        print('formvalidated')
        question = form.question.data
        answer = form.answer.data
        option1 = form.option1.data # Get rid of an option and make it equal an answer
        option2 = form.option2.data
        option3 = form.option3.data
        option4 = form.option4.data
        new_Q = QuestionsOptionsAnswers(question = question, answer = answer, option1 = option1, option2 = option2, option3 = option3, option4 = option4)
        db.session.add(new_Q)
        db.session.commit()
        return redirect(url_for('answer_q', question_id = new_Q.question_id))
    return render_template('create_q.html', form = form)

# Read
@app.route('/view_questions')
def view_questions():
    QOA = map(str, QuestionsOptionsAnswers.query.all())
    return render_template('view_questions.html', QOA = QOA)

# How are you going to get it to go to the next question? One Page?
# I'm not sure the if statement is in the right place or correct
# Better version on "testingthingsout.py"
#@app.route('/answer_questions/<int:q_id>', methods = ['GET', 'POST'])
#def answer_q(question_id):
    form = answer_questionsForm()
    QOAs = QuestionsOptionsAnswers.query.filter_by(question_id = question_id).first()
    option1 = QuestionsOptionsAnswers.option1
    option2 = QuestionsOptionsAnswers.option2
    option3 = QuestionsOptionsAnswers.option3
    option4 = QuestionsOptionsAnswers.option4
    if option1 == "answer":
        print("Correct!")
    else:
        print("Incorrect")
    if option2 == 'answer':
        print("Correct")
    else:
        print("Incorrect")
    if option3 == 'answer':
        print("Correct")
    else:
        print("Incorrect")
    if option4 == 'answer':
        print("Correct")
    else:
        print("Incorrect")
        return redirect(url_for('answer_questions', question_id = question_id + 1))
    return render_template('answeing.html', form = form)

@app.route('/answer_questions/<int:question_id>', methods = ['GET', 'POST'])
def answer_q(question_id):
    form = answer_questionsForm()
    QOAs = QuestionsOptionsAnswers.query.filter_by(question_id = question_id).first()
    form.answer.choices = [(QOAs.option1,QOAs.option1),(QOAs.option2,QOAs.option2),(QOAs.option3,QOAs.option3),(QOAs.option4,QOAs.option4)]
    if request.method == 'POST':
        if form.answer.data == QOAs.answer:
            message = 'correct!'
        else:
            message = 'incorrect'
        return render_template('answering.html', form = form, QOAs = QOAs, message = message)
    # def store_answers(option1, option2, option3, option4, answer):
    #     correct_answers = []
    #     if input(option1) == answer:
    #         print("Correct!")
    #         correct_answers.append(answer)
    #     elif input(option2) == answer:
    #         print("Correct!")
    #         correct_answers.append(answer)
    #     elif input(option3) == answer:
    #         print("Correct!")
    #         correct_answers.append(answer)
    #     elif input(option4) == answer:
    #         print("Correct!")
    #         correct_answers.append(answer)
    #     else:
    #         print("Incorrect!")
    #         return redirect(url_for('answer_questions', question_id = question_id + 1))
    return render_template('answering.html', form = form, QOAs = QOAs, message = None)

# Update
@app.route('/update_questions/<int:question_id>', methods = ['GET', 'POST'])
def update_questions(question_id):
    question_to_update = QuestionsOptionsAnswers.query.get(question_id) # something wrong with this line (Maybe you need data first?)
    form = create_questions_options_answersForm()
    if request.method == 'POST':
        question = form.question.data
        answer = form.answer.data
        option1 = form.option1.data
        option2 = form.option2.data
        option3 = form.option3.data
        option4 = form.option4.data
        question_to_update.question = question if question else question_to_update.question
        question_to_update.answer = answer if answer else question_to_update.answer
        question_to_update.option1 = option1 if option1 else question_to_update.option1
        question_to_update.option2 = option2 if option2 else question_to_update.option2
        question_to_update.option3 = option3 if option3 else question_to_update.option3
        question_to_update.option4 = option4 if option4 else question_to_update.option4
        db.session.commit()
        return redirect(url_for('view_questions'))
    return render_template('update_q.html', form = form)

# Delete
@app.route('/delete_questions/<int:question_id>')
def delete_questions(question_id):
    question_to_delete = QuestionsOptionsAnswers.query.get(question_id) # Something wrong with this line (Maybe you need data first?)
    db.session.delete(question_to_delete)
    db.session.commit()
    return redirect(url_for('view_questions')) # No html template needed

@app.route('/results')
def results():
    results = Results.query.all() # Something wrong with this line (Maybe you need data first?)
    correct_answers = [] # Added
    quiz_results = len(correct_answers)# Added
    return '<br>'.join(results), render_template('results.html', quiz_results = quiz_results)

# Delete
@app.route('/delete_results')
def delete_results(user_id):
    results_to_delete = Results.query.get(user_id)
    db.session.delete(results_to_delete)
    db.session.commit()
    return redirect(url_for('Login_page'))

