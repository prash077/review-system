from django.db import models

class reviews(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10,null=True,blank=True)
    
    def __str__(self):
        return self.text[:50]

