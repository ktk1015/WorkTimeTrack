from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class WorkTime(models.Model):
    work_id = models.AutoField(db_column='id', primary_key=True)
    start_time = models.DateTimeField(db_column='start_time', blank=True, null=True)
    end_time = models.DateTimeField(db_column='end_time', blank=True, null=True)
    user_id = models.ForeignKey(User)

    class Meta:
        managed = False
        db_table = "work_time"
