from click import format_filename
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
# Tasks is being maintained by sqlalchemy, so don't need it here. What should you not include here?

class LoginForm(FlaskForm):
    forname = StringField('Enter forename ')
    surname = StringField('Enter surname ')
    username = StringField('Enter username ')
    submit = SubmitField('Confirm')

# You should only have 3 options and make the answer == optionX
class create_questions_options_answersForm(FlaskForm):
    question = TextAreaField('Type in your question ')
    answer = TextAreaField('Type the answer to the question ')
    option1 = TextAreaField('Type in an optional answer for the question ')
    option1_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    option2 = TextAreaField('Type in an optional answer for the question ')
    option2_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    option3 = TextAreaField('Type in an optional answer for the question ')
    option3_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    option4 = TextAreaField('Type in an optional answer for the question ')
    option4_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    submit = SubmitField('Confirm')

# Maybe put the if correct/incorrect statement here??
class answer_questionsForm(FlaskForm):
    answer = SelectField('Answer', choices = [])

    submit = SubmitField('Confirm') # Try to find out how to make it so that you can click an option instead of typing in an answer from the options

# This would be based on question id
class update_questionsForm(FlaskForm):
    question = TextAreaField('Type in your question ')
    answer = TextAreaField('Type the answer to the question ')
    option1 = TextAreaField('Type in an optional answer for the question ')
    option1_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    option2 = TextAreaField('Type in an optional answer for the question ')
    option2_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    option3 = TextAreaField('Type in an optional answer for the question ')
    option3_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    option4 = TextAreaField('Type in an optional answer for the question ')
    option4_status = SelectField('Correct/incorrect', choices=[('correct','Correct'),('incorrect','Incorrect')])
    submit = SubmitField('Confirm')



