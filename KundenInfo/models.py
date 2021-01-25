from django.db import models

# Create your models here.
class Kundeninfo_Jira(models.Model):
    Fullname = models.CharField(max_length=100)
    E_Mail = models.EmailField(max_length=200)
    Benutzername = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Fullname}"

class Kundeninfo_Portal(models.Model):
    FullnameP = models.CharField(max_length=100)
    E_MailP = models.EmailField(max_length=200)
    BenutzernameP = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.FullnameP}"

