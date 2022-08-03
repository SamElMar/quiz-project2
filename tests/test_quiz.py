from urllib import response
from flask import redirect, url_for
from application import app, db
from application.models import *
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-app.db',
            WTF_CSRF_ENABLED = False,
            DEBUG = True,
            SECRET_KEY = 'DGFSAEHTGRFEWE'
        )

        return app

    def setUp(self):
        db.create_all()
        user1 = Login(forename = 'SampleForename', surname = 'SampleSurname', username = 'Sample123')
        qset = QuestionsOptionsAnswers(question = 'Which country of these countries has a dragon on its flag?', answer = 'Wales', option1 = 'Mexico', option2 = 'Wales', option3 = 'China', option4 = 'Oman')
        db.session.add(user1)
        db.session.add(qset)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testHomeView(TestBase): # Bottom lines probably incorrect
    def test_get_login(self): # Failed
        response = self.client.get(
            url_for('Login_page'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'forename', response.data)

    def test_get_create(self): # Failed
        response = self.client.get(
            url_for('create_questions_options_answers'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'question', response.data)

    def test_get_view_q(self):
        response = self.client.get(url_for('view_questions'))
        self.assert200(response)
        self.assertIn(b'Questions, Options and Answers', response.data)

    def test_get_answer(self): #Failed
        response = self.client.get(url_for('answer_q', question_id = 1))
        self.assert200(response)
        self.assertIn(b'Which country of these countries has a dragon on its flag?', response.data)

    def test_get_update_q(self): # Failed
        response = self.client.get(
            url_for('update_questions', question_id = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'question', response.data)

    def test_get_delete_q(self):
        response = self.client.get(
            url_for('delete_questions', question_id = 1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertNotIn(b'Which country of these countries has a dragon on its flag?, Wales, Mexico, Wales, China, Oman', response.data)

class TestPostRequests(TestBase):
    def test_post_add_u(self):
        response = self.client.post(
            url_for('Login_page'), # This url isnt working
            data = dict(forname = 'Molly', surname = 'Allen', username = 'Mollen'),
            follow_redirects = True
        )
        self.assert200(response)
        #self.assertIn(b'Molly', response.data)
        assert Login.query.filter_by(forename = 'Molly').first() is not None
    
    def test_post_add_q(self):
        response = self.client.post(
            url_for('create_questions_options_answers'),
            data = dict(question = 'Whats up?', answer = 'working', option1 = 'not much', option2 = 'working', option3 = 'chllin', option4 = 'the sky'),
            follow_redirects = True
        )
        self.assert200(response)
        #self.assertIn(b'Whats up', response.data)
        assert QuestionsOptionsAnswers.query.filter_by(question = 'Whats up?').first() is not None

    def test_post_update_q(self):
        response = self.client.post(
            url_for('update_questions', question_id = 1),
            data = dict(question = 'Whats down?', answer = 'dont know', option1 = 'dont know', option2 = 'ground', option3 = 'what?', option4 = 'sky'),
            follow_redirects = True
            
        )
        self.assert200(response)
        assert QuestionsOptionsAnswers.query.filter_by(question = 'Whats down?').first() is not None

    def test_post_answer(self):
        response = self.client.post(
            url_for('answer_q', question_id = 1),
            data = dict(answer = 'dont know'),
        )
        self.assert200(response)
        #assert QuestionsOptionsAnswers.query.filter_by(answer = 'dont know').first() is not None