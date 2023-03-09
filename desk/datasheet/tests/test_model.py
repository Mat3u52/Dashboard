from django.test import TestCase
from datasheet.models import Guideline
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Zenek')
        self.guideline = Guideline.objects.create(
            title='testModel',
            version='0.1',
            text='textModel',
            author_id=self.user.id,
            image='image.png',
        )