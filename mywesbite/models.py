from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.start_year = self.start_date.year
        self.end_year = self.end_date.year
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.company}"
    

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    institute = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.start_year = self.start_date.year
        self.end_year = self.end_date.year
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.degree} - {self.institute}"
    

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ProgrammingSkill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons/', null=True, blank=True, validators=[FileExtensionValidator(['svg'])])

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    


