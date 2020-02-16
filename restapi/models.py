# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comics(models.Model):
    rowid = models.IntegerField(db_column='rowid', primary_key=True)
    title = models.TextField(db_column='title', blank=True, null=True)
    date = models.TextField(db_column='date', blank=True, null=True)
    chapter = models.TextField(db_column='chapter', blank=True, null=True)
    appendix = models.IntegerField(db_column='Appendix', blank=True, null=True)  # Field name made lowercase.
    bladder = models.IntegerField(db_column='Bladder', blank=True, null=True)  # Field name made lowercase.
    bowels = models.IntegerField(db_column='Bowels', blank=True, null=True)  # Field name made lowercase.
    brain = models.IntegerField(db_column='Brain', blank=True, null=True)  # Field name made lowercase.
    derpytooth = models.IntegerField(db_column='DerpyTooth', blank=True, null=True)  # Field name made lowercase.
    esophagus = models.IntegerField(db_column='Esophagus', blank=True, null=True)  # Field name made lowercase.
    eyes = models.IntegerField(db_column='Eyes', blank=True, null=True)  # Field name made lowercase.
    gallbladder = models.IntegerField(db_column='Gallbladder', blank=True, null=True)  # Field name made lowercase.
    heart = models.IntegerField(db_column='Heart', blank=True, null=True)  # Field name made lowercase.
    kidney = models.IntegerField(db_column='Kidney', blank=True, null=True)  # Field name made lowercase.
    kingthyroid = models.IntegerField(db_column='KingThyroid', blank=True, null=True)  # Field name made lowercase.
    liver = models.IntegerField(db_column='Liver', blank=True, null=True)  # Field name made lowercase.
    lungs = models.IntegerField(db_column='Lungs', blank=True, null=True)  # Field name made lowercase.
    pancreas = models.IntegerField(db_column='Pancreas', blank=True, null=True)  # Field name made lowercase.
    spleen = models.IntegerField(db_column='Spleen', blank=True, null=True)  # Field name made lowercase.
    stomach = models.IntegerField(db_column='Stomach', blank=True, null=True)  # Field name made lowercase.
    tongue = models.IntegerField(db_column='Tongue', blank=True, null=True)  # Field name made lowercase.
    tonsils = models.IntegerField(db_column='Tonsils', blank=True, null=True)  # Field name made lowercase.
    trachea = models.IntegerField(db_column='Trachea', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='image', blank=True, null=True)

    class Meta:
        db_table = 'comics'
