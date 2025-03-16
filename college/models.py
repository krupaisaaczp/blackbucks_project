from django.db import models

# Admin Panel Model
class AdminPanel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Exam Model
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    date = models.DateField()
    time = models.TimeField()
    syllabus = models.FileField(upload_to='syllabus/')

    def __str__(self):
        return f"{self.course.name} - {self.date}"

# Study Material Model
class Material(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='materials/')

    def __str__(self):
        return self.name

# Fee Structure Model
class Fee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='fees')
    duration = models.CharField(max_length=50)
    fee = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.name} - {self.duration}"
