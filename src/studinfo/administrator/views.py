from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import Studentdetails, notice, exam,fee
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic import View


# Create your views here.

def login(request):
    return render(request, 'login.html', {})

#def s_details(request):
   # return render(request, 'student_details.html', {})

#student registraion
def studlog(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        name = full_name.split()
        first_name = name[0]
        last_name = name[-1]
        rollnumber = request.POST['rollnumber']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=rollnumber).exists():
                print('The Username exists')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=rollnumber, email=email,
                                                 password=password1)
                user.save()
                print('user created')
                return redirect('/student')
        else:
            print('password wrng')
            return redirect('/student/studlog')
    else:
        return render(request, 'studlog.html', {})

#verifying login
def signin_verify(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/student')
        else:
            messages.info(request,'invalid creditional, please check and try again')
            return redirect('/student/login')
    print('invalid here')
    return redirect('/student/login')

#home page
def home_page(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('/student/login')


#student details being entered, no use as of now.
def s_details(request):
    pass
       # register = reg.object.create(name="name", gender="gender", password="password", rollno = "rollno", date="dob", course = "course", batch="batch")
       # reg.save()
       # print("Student details saved into the Database")


   # return render(request,'student_details.html')



def profile(request):
    student = Studentdetails.objects.get(user=request.user) #remember the code
    return render(request, 'Profile.html', {'student': student})



def notices(request):
    memo = notice.objects.all()
    print(memo)
    return render(request, 'noticeboard.html', {'memo': memo })


def fees(request):
    username = None
    username = request.user.username
    print(username)
    info = fee.objects.all() #credit card payment
    return render(request, 'admin_exam.html', { 'info':info }) #feepayment


def payment(request):
    return render(request, 'payment.html', {})


def bill(request):
    # details = fee.objects.get(user=request.user) #remember the code , invoice
    # return render(request, 'admin_fee.html', {'details' : details})  #admin_fee.html
    dets = fee.objects.all()
    return render(request, 'admin_fee.html', { 'dets':dets })

def examdetails(request):
    details = exam.objects.all()
    return render(request, 'exam.html', { 'details':details } )


# class FeesView(View):
#    def get(self, *args, **kwargs):
#        try:
#
#            # # getting logged in stdeunts data from student details table
#            # get_student_data = StudentDetails.objects.get(user=self.request.user)
#            # course_name = get_student_data.coursename  # getting course name from student details
#            #
#            # # fetching the fee details from fee list based on the course
#            # fee_qs = Fee.objects.get(course=course_name)
#            # if fee_qs.exists():
#            #     fees = fee_qs[0]
#            #     if FeePaid.objects.get()
#            # # checking fee paid model, whether that particular student paid the fees.
#            # if FeePaid.objects.get(user=self.request.user, fee=feename).exists():
#            #     print("no pending fees")
#            #     context = {
#            #
#            #     }
#            print("fees sections")
#            return render(self.request, 'admin_exam.html', {})
#        except ObjectDoesNotExist:
#            return render(self.request, 'admin_exam.html', {})
