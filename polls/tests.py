from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Question, Choice

class VoteAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="pass123")
        self.question = Question.objects.create(question_text="Test Question?")
        self.choice = Choice.objects.create(question=self.question, choice_text="Yes", votes=0)

    def test_vote_requires_login(self):
        response = self.client.post(reverse('polls:vote', args=[self.question.id]), {
            'choice': self.choice.id
        })
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login

    def test_vote_after_login(self):
        self.client.login(username="testuser", password="pass123")
        response = self.client.post(reverse('polls:vote', args=[self.question.id]), {
            'choice': self.choice.id
        })
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)
