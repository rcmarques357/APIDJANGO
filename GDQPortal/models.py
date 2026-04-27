from django.db import models
from datetime import date

class ProcessInformation(models.Model):
    STATUS_CHOICES=[('not_started','Not Started'), ('planned','Planned'),('in_progress', 'In Progress'),('on_hold','On Hold'),('cancelled','Cancelled'),('blocked','Blocked'),('completed',"Completed")]
    process_number = models.CharField(max_length=10, unique=True)
    process_name = models.CharField(max_length=255)
    process_issue = models.CharField(max_length=1500)
    process_solution = models.CharField(max_length=1500)
    process_benefits = models.CharField(max_length=1500)
    process_start_date = models.DateField(null=True, blank=True, default=date.today)
    process_completion_date = models.DateField(null=True, blank=True)
    process_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not_started")

    def __str__(self):
        return f"{self.process_number} - {self.process_name}"
    
# Create your models here.
