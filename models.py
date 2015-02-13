import re
from functools import reduce
import operator

from django.db import models
from django.utils.html import escape
from django.core.urlresolvers import reverse

from mainstay.models import UpdatedAndCreated


class PageManager(models.Manager):
    """From http://toastdriven.com/blog/2008/nov/09/quick-dirty-search-django/"""
    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        q_objects = []

        for term in terms:
            q_objects.append(models.Q(title__icontains=term))
            q_objects.append(models.Q(content__icontains=term))

        # Start with a bare QuerySet
        qs = self.get_queryset()

        # Use operator's or_ to string together all of your Q objects.
        return qs.filter(reduce(operator.or_, q_objects))


class Page(UpdatedAndCreated, models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    objects = PageManager()

    def as_html(self):
        def match_replace(match):
            val = match.group(1)
            return '<a href="{0}">{1}</a>'.format(
                reverse('mainstay_wiki:page', args=(val,)), escape(val))
        return re.sub(r'\[\[(.*)\]\]', match_replace, escape(self.content))
