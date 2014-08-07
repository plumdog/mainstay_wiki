from datetime import datetime
import re

from django.db import models
from django.utils.html import escape
from django.core.urlresolvers import reverse


class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.today()
        self.updated_at = datetime.today()
        return super(Page, self).save(*args, **kwargs)

    def as_html(self):
        def match_replace(match):
            val = match.group(1)
            return '<a href="{0}">{1}</a>'.format(
                reverse('mainstay_wiki:page', args=(val,)), escape(val))
        return re.sub(r'\[\[(.*)\]\]', match_replace, escape(self.content))
