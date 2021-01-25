from django.db import models

# Create your models here.
class CSV_JiraDB(models.Model):
    file_name= models.FileField(upload_to='csvCompare')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"