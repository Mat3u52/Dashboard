from django.test import SimpleTestCase
from datasheet.forms import GuideForm


class TestForm(SimpleTestCase):

    def test_form_valid_data(self) -> None:
        """
        Validate data
        :return: Prepared data
        :rtype: None
        """
        form = GuideForm(data={
            'title': 'testTitleForm',
            'version': '0.1',
            'text': 'textTestForm',
            'image': 'imageTestForm.png'
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self) -> None:
        """
        Valid form
        :return: Valid form
        :rtype: None
        """
        form = GuideForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
