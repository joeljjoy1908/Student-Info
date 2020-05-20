from django.contrib import admin
from .models import Studentdetails,marks,course,subject,notice,exam,Dept,fee

# Register your models here.

admin.site.register(Studentdetails)
admin.site.register(marks)
admin.site.register(course)
admin.site.register(subject)
admin.site.register(notice)
admin.site.register(Dept)
admin.site.register(exam)
admin.site.register(fee)
# admin.site.register(FeePaid)
