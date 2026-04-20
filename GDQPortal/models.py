from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

class ProcessInformation(models.Model):
    STATUS=[('not started','Not Started'), ('planned','Planned'),('in progress', 'In Progress'),('on hold','On Hold'),('cancelled','Cancelled'),('blocked','Blocked'),('completed',"Completed")]
    process_number = models.CharField(max_length=10)
    process_name = models.CharField(max_length=255)
    process_issue = models.CharField(max_length=1500)
    process_solution = models.CharField(max_length=1500)
    process_benefits = models.CharField(max_length=1500)
    process_start_date = models.DateField(null=True, blank=True, default=date.today)
    process_completion_date = models.DateField(null=True, blank=True)
    process_status = models.CharField(max_length=20, choices=STATUS, default="notstarted")

    def __str__(self):
        return self.process_name
    

class ProcessKPIInformation(models.Model):
    FREQUENCY=[('weekly','Weekly'),('biweekly','Biweekly'),('monthly','Monthly'),('quartely','Quartely'),('biannually','Biannually'),('annually','Annually')]
    kpi_name = models.CharField(max_length=255)
    kpi_business_impact = models.CharField(max_length=500)
    kpi_measurement_method = models.CharField(max_length=500)

    def _str_(self):
        return self.kpi_name

class ProcessKPIValue(models.Model):
    kpi_name = models.CharField(max_length=255)
    kpi_measurement_value = models.CharField(max_length=500)
    kpi_measurement_Date = models.DateField(default=date.today)

    def _str_(self):
        return self.kpi_name
    

class ProcessTask(models.Model):
    TASKSTATUS=[("notstarted","Not Started"),("inprogress", "In Progress"),("onhold","On Hold"),("cancelled","Cancelled"),("blocked","Blocked")]
    task_process_number = models.CharField(max_length=10)
    task_name = models.CharField(max_length=255)
    task_start_date = models.DateField(default=date.today)
    task_completion_date = models.DateField()
    task_status = models.CharField(max_length=20, choices=TASKSTATUS, default="notstarted")
    task_weight = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def _str_(self):
        return self.task_name

# Create your models here.
