from django.test import TestCase
from .models import PortofolioItem

class PortofolioItemModelTest(TestCase):

    def setUp(self):
        self.item = PortofolioItem.objects.create(
            title='Test Title',
            description='Test Description',
            image='path/to/image.jpg'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.item), self.item.title)

    def test_title_max_length(self):
        max_length = self.item._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)