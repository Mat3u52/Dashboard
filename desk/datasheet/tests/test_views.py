from django.test import TestCase, Client
from django.urls import reverse
from datasheet.models import Guideline
from django.contrib.auth.models import User


# title = serializers.CharField(max_length=250)
# version = serializers.CharField(max_length=10)
# text = serializers.CharField()
# created_date = serializers.DateTimeField()
# publish_date = serializers.DateTimeField()
# image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url='images/')

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.guideline_list_url = reverse('guideline_list')
        self.guideline_new_url = reverse('guide_new')
        self.guideline_detail_url = reverse('guideline_detail', args=['1'])

        self.user = User.objects.create(username='Zenek')
        self.product1 = Guideline.objects.create(
            title='test',
            version='0.1',
            text='text',
            author_id=self.user.id,
            image='image.png',
        )

    def test_guideline_list_GET(self):
        response = self.client.get(self.guideline_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'datasheet/guideline_list.html')

    def test_guideline_detail_GET(self):
        response = self.client.get(self.guideline_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'datasheet/guideline_detail.html')

    def test_guide_new_POST(self):
        self.product2 = Guideline.objects.create(
            title='test02',
            version='0.2',
            text='text01',
            author_id=self.user.id,
            image='image01.png',
        )

        response = self.client.post(self.guideline_detail_url, {
            'title': 'test02',
            'version': '0.3',
            'text': 'text02',
            'author_id': self.user.id,
            'image': 'image02.png',
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.product2.title, 'test02')

    # def test_guide_new_create_POST(self):
    #
    #     url = reverse('guide_new')
    #     response = self.client.post(url, {
    #         'title': 'test06',
    #         'version': '0.5',
    #         'text': 'text05',
    #         'author_id': self.user.id,
    #         'image': 'image05.png',
    #     })
    #     project3 = Guideline.objects.get(id=2)
    #     self.assertEquals(project3.title, 'test06')



