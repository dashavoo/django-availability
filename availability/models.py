# coding: utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import datetime

@python_2_unicode_compatible
class Availability(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return("%s - %s" % (self.start_date.isoformat(), self.end_date.isoformat()))
    
    def generate_dates(self):
        return (self.start_date + datetime.timedelta(days=d) for d in xrange((self.end_date - self.start_date).days + 1))

    class Meta:
        unique_together = (("start_date", "end_date", "content_type", "object_id"))
        verbose_name_plural = "Availability"
