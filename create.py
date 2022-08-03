from application import db
from application.models import Login, QuestionsOptionsAnswers, QuestionAssociation, Results
# Do you need to include the question association class?

db.drop_all()
db.create_all()

user1 = Login(forename = "Sam", surname = "Marten", username = "SMARTEN")
question_set1 = QuestionsOptionsAnswers(question = "How many legs do dogs have?", answer = "4", option1 = "2", option2 = "6", option3 = "4", option4 = "75")
#QAss1 = QuestionAssociation(use_id = "1", question_id = "1")
results1 = Results(quiz_results = "6", time_to_complete = "180")
db.session.add(user1)
db.session.add(question_set1)
#db.session.add(QAss1)
db.session.add(results1)
db.session.commit()

print(user1)
print(question_set1)
#print(QAss1)
print(results1)
