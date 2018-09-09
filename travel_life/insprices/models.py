# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AlliplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'alliplan_med'


class AlliplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'alliplan_nomed'


class BerkplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'berkplan_med'


class BerkplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'berkplan_nomed'


class ManuplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'manuplan_med'


class ManuplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'manuplan_nomed'


class TicplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'ticplan_med'


class TicplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'ticplan_nomed'

class GMSplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'gmsplan_med'

class GMSplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'gmsplan_nomed'

class TugoplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_20k = models.FloatField(blank=True, null=True)
    cov_30k = models.FloatField(blank=True, null=True)
    cov_40k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_60k = models.FloatField(blank=True, null=True)
    cov_80k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    cov_200k = models.FloatField(blank=True, null=True)
    cov_250k = models.FloatField(blank=True, null=True)
    cov_300k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'tugoplan_med'

class TugoplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_20k = models.FloatField(blank=True, null=True)
    cov_30k = models.FloatField(blank=True, null=True)
    cov_40k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_60k = models.FloatField(blank=True, null=True)
    cov_80k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    cov_200k = models.FloatField(blank=True, null=True)
    cov_250k = models.FloatField(blank=True, null=True)
    cov_300k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'tugoplan_nomed'

class TfirstplanNomed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'tfirstplan_nomed'

class TfirstplanMed(models.Model):
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    cov_10k = models.FloatField(blank=True, null=True)
    cov_15k = models.FloatField(blank=True, null=True)
    cov_25k = models.FloatField(blank=True, null=True)
    cov_50k = models.FloatField(blank=True, null=True)
    cov_100k = models.FloatField(blank=True, null=True)
    cov_150k = models.FloatField(blank=True, null=True)
    plan_id = models.AutoField(primary_key=True)

    def __str__(self):
        return "Age: " + str(self.age_from) + " - " + str(self.age_to)

    class Meta:
        db_table = 'tfirstplan_med'