from django.test import TestCase
from django.contrib.auth.models import User
from mainstay.test_utils import MainstayTest

from .models import Page


class WikiTestCase(MainstayTest):
    fixtures = MainstayTest.fixtures + ['wiki_pages']

    def test_user_loaded(self):
        user = User.objects.get()
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.is_superuser, True)

    def test_pages_loaded(self):
        pages = Page.objects.all()
        self.assertEqual(len(pages), 2)

    def test_page_view(self):
        self.login()
        r = self.client.get('/wiki/page/TestPage')

    def test_page_with_link(self):
        self.login()
        r = self.client.get('/wiki/page/PageWithLink')
        self.assertInHTML('<a href="/wiki/page/TestPage">TestPage</a>', r.content.decode('utf-8'))

    def test_search(self):
        self.login()
        r = self.client.get('/wiki/search/page')
        results = r.context['results']
        self.assertEqual({r.title for r in results}, {'TestPage', 'PageWithLink'})

        r = self.client.get('/wiki/search/withlink')
        results = r.context['results']
        self.assertEqual({r.title for r in results}, {'PageWithLink'})

    def test_add_page(self):
        self.login()
        self.assertEqual(Page.objects.count(), 2)
        post = {'title': 'NewTitle',
                'content': 'NewContent'}
        r = self.client.post('/wiki/add/', post, follow=True)
        self.assertRedirects(r, '/wiki')

    def test_edit_page(self):
        self.login()
        self.assertEqual(Page.objects.count(), 2)
        post = {'title': 'NewTitle',
                'content': 'NewContent'}
        r = self.client.post('/wiki/edit/TestPage', post, follow=True)
        self.assertRedirects(r, '/wiki/page/NewTitle')
