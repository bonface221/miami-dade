from django.contrib.auth.models import User
from django.db import models



# this is the model for the first search here is the link to the searched website 'https://onlineservices.miami-dadeclerk.com/officialrecords/StandardSearch.aspx'
class OfficialSearch(models.Model):
    Clerks_File_No = models.CharField(max_length=255)
    Doc_Type = models.CharField(max_length=255, blank=True)
    Rec_Date = models.DateField()
    Rec_Book_or_Page = models.CharField(max_length=255)
    Plat_Book_or_Page = models.CharField(max_length=255)
    Blk = models.CharField(max_length=255, blank=True)
    Legal = models.CharField(max_length=255, blank=True)
    Misc_Ref = models.CharField(max_length=255, blank=True)
    First_Party_Code = models.CharField(max_length=255, blank=True)
    Second_Party_Code = models.CharField(max_length=255, blank=True)


# Model for the second search
# Official record section
class Parties(models.Model):
    party_description = models.CharField(max_length=255, blank=True)
    party_name = models.CharField(max_length=100)
    # can be null
    attorney_information = models.CharField(max_length=100, blank=True)
    attorney_name = models.CharField(max_length=100, blank=True)
    local_case_number = models.CharField(max_length=100,blank=True)


class Dockets(models.Model):
    event_date = models.CharField(max_length=100)
    docket_number = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    book_page = models.CharField(max_length=100, blank=True)
    docket_entry = models.CharField(max_length=100, blank=True)
    event_type = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

# add a case class that combines parties and docket as a many to many relationship


class Case(models.Model):
    local_case_number = models.CharField(max_length=100)
    case_type=models.CharField(max_length=100,null=True)
    state_number=models.CharField(max_length=100,null=True)
    parties = models.ManyToManyField(Parties)
    dockets = models.ManyToManyField(Dockets)
