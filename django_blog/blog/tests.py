from django.test import TestCase
from .models import ArticleModel
from datetime import datetime
from django.utils import timezone


# Create your tests here.


class ArticleTest(TestCase):
    """
    docstring
    """

    def test_article_created_success(self):
        """
        docstring
        """
        ArticleModel.objects.create(title='test article', category='test category', author='test author',
                                    content='test content', creation_date=datetime.now(tz=timezone.utc))
        article = ArticleModel.objects.get(title='test article')
        self.assertEqual(article.category, 'test category')


class BlogPagesTest(TestCase):
    """
    docstring
    """

    def test_home_page_content(self):
        """
        docstring
        """
        res = self.client.get('/blog/')
        self.assertEqual(res.content, b'Welcome to my blog!')
