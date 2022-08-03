from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from application import db
# Do you need to say where the primary keys are used elsewhere, similarly to the foreign keys? 

class Login(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(20), nullable = False)
    surname = db.Column(db.String(20), nullable = False)
    username = db.Column(db.String(20), nullable = False)
    login_QOA = db.relationship('QuestionAssociation', backref = 'Login')
    Login_Results = db.relationship('Results', backref = 'Login')

# How to create the relationships between the different tables?

class QuestionsOptionsAnswers(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable = False)
    answer = db.Column(db.Text, nullable = False)
    option1 = db.Column(db.Text, nullable = False) # Get rid of one of the options and make it == answer
    option2 = db.Column(db.Text, nullable = False)
    option3 = db.Column(db.Text, nullable = False)
    option4 = db.Column(db.Text, nullable = False)
    QOA_Results = db.relationship('Results', backref = 'QuestionsOptionsAnswers')

class QuestionAssociation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("login.user_id"))
    question_id = db.Column(db.Integer, db.ForeignKey('questions_options_answers.question_id'))
    QAss_QOA = db.relationship('QuestionsOptionsAnswers', backref = 'QuestionAssociation')

class Results(db.Model):
    results_id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions_options_answers.question_id'))
    quiz_results = db.Column(db.Integer, nullable = False)
    time_to_complete = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.user_id'))


    