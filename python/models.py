# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    cardid = models.CharField(db_column='CardID', primary_key=True, max_length=255)  # Field name made lowercase.
    drawerid = models.CharField(db_column='DrawerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardtext = models.CharField(db_column='CardText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardnumber = models.CharField(db_column='CardNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardgroup = models.CharField(db_column='CardGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationnumber = models.CharField(db_column='RegistrationNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=255, blank=True, null=True)  # Field name made lowercase.
    claimant = models.CharField(db_column='Claimant', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timeframe = models.CharField(db_column='TimeFrame', max_length=255, blank=True, null=True)  # Field name made lowercase.
   
    class Meta:
        db_table = 'Cards'


class Comments(models.Model):
    commendid = models.CharField(db_column='CommendID', primary_key=True, max_length=255)  # Field name made lowercase.
    commenttext = models.CharField(db_column='CommentText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardid = models.CharField(db_column='CardID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromname = models.CharField(db_column='FromName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromtitle = models.CharField(db_column='FromTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromphone = models.CharField(db_column='FromPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromaddress = models.CharField(db_column='FromAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fromemail = models.CharField(db_column='FromEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Comments'


class Drawers(models.Model):
    drawerid = models.CharField(db_column='DrawerID', primary_key=True, max_length=255)  # Field name made lowercase.
    drawerpath = models.CharField(db_column='DrawerPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drawerdescription = models.CharField(db_column='DrawerDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timeframe = models.CharField(db_column='TimeFrame', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Drawers'


class Feedback(models.Model):
    feedbackid = models.AutoField(db_column='FeedbackID', primary_key=True)  # Field name made lowercase.
    feedbacktext = models.CharField(db_column='FeedbackText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    feedbackcategory = models.CharField(db_column='FeedbackCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    feedbackcardid = models.CharField(db_column='FeedbackCardID', max_length=255, blank=True, null=True)  # Field name made lowercase.
     
    class Meta:
        db_table = 'Feedback'


class Projectproperties(models.Model):
    parameter = models.CharField(db_column='Parameter', primary_key=True, max_length=255)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ProjectProperties'


class Timeframes(models.Model):
    timeframe = models.CharField(db_column='TimeFrame', primary_key=True, max_length=255)  # Field name made lowercase.
    timeframedescription = models.CharField(db_column='TimeFrameDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'TimeFrames'
