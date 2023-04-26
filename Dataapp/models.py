from django.db import models

# Create your models here.
class all_user(models.Model):
    ID = models.IntegerField(primary_key=True)
    Password = models.CharField(max_length=100)
    User_type = models.CharField(max_length=30)

class Faculties(models.Model):
    Name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(primary_key=True)
    address = models.CharField(max_length=200)

class Student(models.Model):
    studentID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField( max_length=50)
    departmentID = models.CharField(max_length=50)
    programID = models.CharField( max_length=50)


class Section(models.Model):
    sectionID = models.AutoField(primary_key=True)
    sectionNum = models.IntegerField()
    semester = models.CharField(max_length=20)
    courseID = models.CharField(max_length=10)
    year = models.IntegerField()


class co_T(models.Model):
    co_ID = models.AutoField(primary_key=True)
    sectionID = models.ForeignKey(Section,on_delete=models.CASCADE)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    co1 = models.FloatField()
    co2 = models.FloatField()
    co3 = models.FloatField()
    co4 = models.FloatField()
    totalCo = models.FloatField()


