from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    # The actual text of the todo
    title = models.CharField(max_length=200)
    
    # A checkbox to mark it as done
    completed = models.BooleanField(default=False)
    
    # Automatically record when the task was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title