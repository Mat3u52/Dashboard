from django.test import SimpleTestCase
from django.urls import reverse, resolve
from datasheet.views import guideline_list, guideline_detail, guide_new, guideline_edit


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('guideline_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, guideline_list)

    def test_detail_url_is_resolved(self):
        url = reverse('guideline_detail', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, guideline_detail)

    def test_new_url_is_resolved(self):
        url = reverse('guide_new')
        print(resolve(url))
        self.assertEquals(resolve(url).func, guide_new)

    def test_edit_url_is_resolved(self):
        url = reverse('guideline_edit', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, guideline_edit)
