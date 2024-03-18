from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    subject = models.CharField(max_length=10, verbose_name='Subject')
    students = models.ManyToManyField('Student', related_name='teachers')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    group = models.CharField(max_length=10, verbose_name='Group')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name
