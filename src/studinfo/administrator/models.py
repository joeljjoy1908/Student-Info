from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Dept(models.Model):
    deptname = models.CharField(max_length=50)
    d_description = models.CharField(max_length=50)

    def __str__(self):
        return self.deptname

class course(models.Model):
    coursename = models.CharField(max_length=50)
    deptname = models.ForeignKey(Dept, on_delete=models.CASCADE, related_name='deptn')

    def __str__(self):
        return self.coursename


class Studentdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userinfo')#rollnumber
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    coursename = models.ForeignKey(course, on_delete=models.CASCADE, related_name='coursen')
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    startbatch = models.IntegerField()
    endbatch = models.IntegerField()
    image = models.ImageField(upload_to='studentimages/', blank=True, null=True)

    def __str__(self):
        return str(self.user)




class subject(models.Model):
    deptname = models.ForeignKey(Dept, on_delete=models.CASCADE, related_name='deptnames')
    coursename = models.ForeignKey(course, on_delete=models.CASCADE, related_name='coursenames')
    subjectname = models.CharField(max_length=50)

    def __str__(self):
        return self.subjectname


class marks(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usernam')
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='cours')
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, related_name='subjec')
    marks = models.IntegerField()


    #view code
class notice(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    venue = models.CharField(max_length=250)
    fromdate = models.DateField()
    todate = models.DateField()

class exam(models.Model):
    description = models.TextField(max_length=250)
    file = models.FileField(upload_to='documemts/', blank=True, null=True)

class fee(models.Model):
    fee_name = models.CharField(max_length=50, blank=True, null=True)
    amount = models.IntegerField()
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='cou')
    student = models.ForeignKey(Studentdetails, on_delete=models.CASCADE, related_name='st')
    due_date = models.DateField(blank=True, null=True)
    pay_status = models.BooleanField(default=False)
    # slug = models.SlugField()

    def __str__(self):
        return self.fee_name


# class FeePaid(models.Model):
#     stud_uname = models.ForeignKey(User, on_delete=models.CASCADE, related_name='studuname')
#     fee = models.ForeignKey(fee, on_delete=models.CASCADE, related_name='fees')
#     course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='co')
#     pay_status = models.BooleanField(default=False)
#

