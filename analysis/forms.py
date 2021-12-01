from django.db import models
from django.forms import ModelForm
from django import forms

YEAR_CHOICES = [('2008','2008'),('2009','2009'),('2010','2010'),
                ('2011','2011'),('2012','2012'),('2013','2013'),
                ('2014','2014'),('2015','2015'),('2016','2016'),
                ('2017','2017'),('2018','2018'),('2019','2019'),
                ('overall','Overall')]

TEAM_CHOICES = [('Royal Challengers Bangalore','Royal Challengers Bangalore'),
                ('Punjab Kings','Punjab Kings'),('Delhi Capitals','Delhi Capitals'),
                ('Mumbai Indians','Mumbai Indians'),
                ('Kolkata Knight Riders','Kolkata Knight Riders'),
                ('Rajasthan Royals','Rajasthan Royals'),
                ('Chennai Super Kings','Chennai Super Kings'),
                ('Kochi Tuskers Kerala','Kochi Tuskers Kerala'),
                ('Pune Warriors','Pune Warriors'),
                ('Sunrisers Hyderabad','Sunrisers Hyderabad'),
                ('Gujarat Lions','Gujarat Lions'),('Rising Pune Supergiant','Rising Pune Supergiant'),
                ('None','None')]

class Filter(models.Model):
    year = models.CharField(max_length=10,choices=YEAR_CHOICES,default='overall')
    team_name = models.CharField(max_length=50,choices=TEAM_CHOICES,default='None')

class Filter_year(models.Model):
    year = models.CharField(max_length=10,choices=YEAR_CHOICES,default='overall')


class UploadFileForm(forms.Form):
    file = forms.FileField()


class FilterForm(ModelForm):
  class Meta:
    model = Filter
    fields = '__all__'

class FilterYearForm(ModelForm):
  class Meta:
    model = Filter_year
    fields = '__all__'
