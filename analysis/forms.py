from django.db import models
from django.forms import ModelForm
from django import forms

YEAR_CHOICES = [('2008','2008'),('2009','2009'),('2010','2010'),
                ('2011','2011'),('2012','2012'),('2013','2013'),
                ('2014','2014'),('2015','2015'),('2016','2016'),
                ('2017','2017'),('2018','2018'),('2019','2019'),
                ('overall','Overall')]
class Filter(models.Model):
    year = models.CharField(max_length=10,choices=YEAR_CHOICES,default='overall')

class UploadFileForm(forms.Form):
    file = forms.FileField()


class FilterForm(ModelForm):
  class Meta:
    model = Filter
    fields = '__all__'