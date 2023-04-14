from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100, choices=(('Web Dev', 'Web Dev'), ('AI/ML', 'AI/ML'), ('Basic Coding', 'Basic Coding')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
