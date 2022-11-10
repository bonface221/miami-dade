from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# this is the model for the first search here is the link to the searched website 'https://onlineservices.miami-dadeclerk.com/officialrecords/StandardSearch.aspx'
class OfficialSearch(models.Model):
    Clerks_File_No = models.CharField(max_length=255)
    Doc_Type = models.CharField(max_length=255)
    Rec_Date = models.DateField()
    Rec_Book_or_Page = models.CharField(max_length=255)
    Plat_Book_or_Page = models.CharField(max_length=255)
    Blk=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    Legal = models.CharField(max_length=255)
    Misc_Ref = models.CharField(max_length=255)
    First_Party_Code = models.CharField(max_length=255)
    Second_Party_Code = models.CharField(max_length=255)


