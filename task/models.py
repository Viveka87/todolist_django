from django.db import models

# Create your models here.
class Notes(models.Model):
    status_choices=[
        ('not_started','Not Yet Started'),
        ('started','Started'),
        ('progress','Progress'),
        ('pending','Pending'),
        ('Completed','Completed'),
    ]
    title=models.CharField(max_length=200)
    #completed=models.BooleanField(default=False)
    completed=models.CharField(max_length=30,choices=status_choices,default='not_started')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

