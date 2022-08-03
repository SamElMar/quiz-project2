from flask import render_template
from application.forms import answer_questionsForm
from application.models import QuestionsOptionsAnswers

def answerstore(answer):
    if "option1" == answer:
        input("option1")

@app.route('/answer_questions/<int:q_id>', methods = ['GET', 'POST'])
def answer_q(question_id):
    form = answer_questionsForm()
    QOAs = QuestionsOptionsAnswers.query.filter_by(question_id = question_id).first()
    option1 = QuestionsOptionsAnswers.option1
    option2 = QuestionsOptionsAnswers.option2
    option3 = QuestionsOptionsAnswers.option3
    option4 = QuestionsOptionsAnswers.option4
    def store_answers(option1, option2, option3, option4, answer):
        correct_answers = []
        if input(option1) == answer:
            print("Correct!")
            correct_answers.append(answer)
        elif input(option2) == answer:
            print("Correct!")
            correct_answers.append(answer)
        elif input(option3) == answer:
            print("Correct!")
            correct_answers.append(answer)
        elif input(option4) == answer:
            print("Correct!")
            correct_answers.append(answer)
        else:
            print("Incorrect!")
            return redirect(url_for('answer_questions', question_id = question_id + 1))
    return render_template('answeing.html', form = form)

answer_list = []
correct_answers = []
number_correct = len(correct_answers)
#RandomChange