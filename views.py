from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def login(request):
    return render(request,'login.html')

def landing(request):
    return render(request,'landing.html')

def about(request):
    return render(request,'about.html')



def adminhome(request):
    return render(request,'adminhome.html')


def landingsubheader(request):
    return render(request,'landingsubheader.html')


def subheader(request):
    return render(request,'subheader.html')

def doctorsubheader(request):
    return render(request,'doctorsubheader.html')

def usersubheader(request):
    return render(request,'usersubheader.html')

def hospitalsubheader(request):
    return render(request,'hospitalsubheader.html')

def admin(request):
    return render(request,'admin.html')

def userregistration(request):
    # id=request.session.get('user_id')
    # userdata=User.objects.get(loginid=id)
    # logindata=Login.objects.get(id=id)
    if request.method=='POST':
        form1=UserForm(request.POST)
        form2=LoginForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            a=form2.save(commit=False)
            a.usertype='USER'
            a.save()
            b=form1.save(commit=False)
            b.loginid=a
            b.save()
            return redirect('userhome')
    else:
          form1=UserForm()
          form2=LoginForm()
    return render(request,'userreg.html',{'form':form1,'forms':form2}) 

def doctorregistration(request):
    if request.method=='POST':
        form1=DoctorForm(request.POST)
        form2=LoginForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            a=form2.save(commit=False)
            a.usertype='DOCTOR'
            a.save()
            b=form1.save(commit=False)
            b.loginid=a
            b.save()
            return redirect('doctorhome')
    else:
          form1=DoctorForm()
          form2=LoginForm()
    return render(request,'doctreg.html',{'form':form1,'forms':form2})

def hospitalregistration(request):
    if request.method=='POST':
        form1=HospitalForm(request.POST)
        form2=LoginForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            a=form2.save(commit=False)
            a.usertype='hospital'
            a.save()
            b=form1.save(commit=False)
            b.Hospital_id=a
            b.save()
            return redirect('hospitalhome')
    else:
          form1=HospitalForm()
          form2=LoginForm()
    return render(request,'hospitalreg.html',{'form':form1,'forms':form2})



def login(request):
    if request.method=='POST':
        form=Customloginform(request.POST)
        print(form)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            if email=='admin@gmail.com' and password=='admin123':
                return redirect('adminhome')

            try:
                user=Login.objects.get(email=email)
                if user.password==password and user.usertype=='USER':
                    request.session['user_id']=user.id
                    return redirect('userhome')
                elif user.password==password and user.usertype=='hospital':
                    request.session['hospital_id']=user.id
                    return redirect('hospitalhome')
                elif user.password==password and user.usertype=='DOCTOR':
                    request.session['doctor_id']=user.id
                    return redirect('doctorhome')
                
                       
                else:
                    messages.error(request, 'Invalid email or password')
            except Login.DoesNotExist:
                messages.error(request, 'User does not exist')
    else:
        form = Customloginform()

    return render(request, 'login.html', {'form': form})
    


def userhome(request):
    return render(request,'userhome.html')

def hospitalhome(request):
    return render(request,'hospitalhome.html')
   
def doctorhome(request):
    return render(request,'doctorhome.html')

def user_edit(request):
    id=request.session.get('user_id')
    userdata=User.objects.get(loginid=id)
    logindata=Login.objects.get(id=id)
    if request.method=='POST':
        form1=UserForm(request.POST,instance=userdata)
        form2=LoginForm(request.POST,instance=logindata)
        if form1.is_valid() and form2.is_valid():
            form2.save()
            form1.save()
            return redirect('userhome')
    else:
          form1=UserForm(instance=userdata)
          form2=LoginForm(instance=logindata)
    return render(request,'user_edit.html',{'form':form1,'forms':form2}) 

def doctor_edit(request):
    id=request.session.get('doctor_id')
    userdata=Doctor.objects.get(loginid=id)
    logindata=Login.objects.get(id=id)
    if request.method=='POST':
        form1=DoctorForm(request.POST,instance=userdata)
        form2=LoginForm(request.POST,instance=logindata)
        if form1.is_valid() and form2.is_valid():
            form2.save()
            form1.save()
            return redirect('doctorhome')
    else:
          form1=DoctorForm(instance=userdata)
          form2=LoginForm(instance=logindata)
    return render(request,'doctor_edit.html',{'form':form1,'forms':form2}) 


def hospital_edit(request):
    id=request.session.get('hospital_id')
    userdata=Hospital.objects.get(Hospital_id=id)
    logindata=Login.objects.get(id=id)
    if request.method=='POST':
        form1=UserForm(request.POST,instance=userdata)
        form2=LoginForm(request.POST,instance=logindata)
        if form1.is_valid() and form2.is_valid():
            form2.save()
            form1.save()
            return redirect('hospitalhome')
    else:
          form1=UserForm(instance=userdata)
          form2=LoginForm(instance=logindata)
    return render(request,'hospital_edit.html',{'form':form1,'forms':form2}) 

def doctor_approve(request, id):
    data=Login.objects.get(id=id)
    data.login_status = 1  # Approved
    data.save()
    return redirect('admin_docview')

def doctor_reject(request,id):
    data=Login.objects.get(id=id)
    data.login_status = 2
    data.save()
    return redirect('admin_docview')

   


def adminhospital_list(request):
    hosp = Hospital.objects.all()
    return render(request,'adminhospital_list.html',{'hosp':hosp})

def adminuser_list(request):
    hosp = User.objects.all()
    return render(request,'adminuser_list.html',{'hosp':hosp})

def admindoctor_list(request):
    hosp = Doctor.objects.all()
    return render(request,'admindoctor_list.html',{'hosp':hosp})

def adminheader(request):
    return render(request,'adminheader.html')

def userdoclist(request):
    doc= Doctor.objects.all()
    query = request.GET.get('q','') 
    

    if query:
        print("hii")
        doc = doc.filter(
            Q(name__icontains=query) |
            Q(gender__icontains=query) |
            Q(qualifications__icontains=query) |
            Q(experience__icontains=query) 
        )
        print("doc=",doc)
    return render(request,'userdoclist.html',{'doc':doc,'query':query})

def appointment(request,did):
    loginid=request.session.get('user_id')
    user=User.objects.get(loginid=loginid)
    doctor=Doctor.objects.get(id=did)
    if request.method=='POST':
        form1=Appointmentform(request.POST)
        if form1.is_valid():
            b=form1.save(commit=False)
            b.user_id=user
            b.doctor_id=doctor
            b.Appointment_status=1
            b.save()
            return redirect('appointment_list')
    else:
          form1=Appointmentform()
    return render(request,'appointment.html',{'form1':form1})

def appointment_list(request):
    loginid=request.session.get('user_id')
    user=User.objects.get(loginid=loginid)
    hosp = Appointment.objects.filter(user_id=user)
    return render(request,'appointment_list.html',{'hosp':hosp})



def appointment_edit(request,id):
    loginid=request.session.get('user_id')
    user=User.objects.get(loginid=loginid)
    appointment_id=Appointment.objects.get(id=id)
    if request.method=='POST':
        form1=Appointmentform(request.POST,instance=appointment_id)
        if form1.is_valid():
            b=form1.save(commit=False)
            b.user_id=user
            b.save()
            return redirect('appointment_list')
    else:
          form1=Appointmentform(instance=appointment_id)
    return render(request,'appointment_edit.html',{'form1':form1})

def appointment_delete(request,id):
    data=Appointment.objects.get(id=id)
    data.delete()
    return redirect('appointment_list')

def doctor_view(request):
    loginid=request.session.get('doctor_id')
    doc=Doctor.objects.get(loginid=loginid)
    hosp = Appointment.objects.filter(doctor_id=doc)
    return render(request,'doctor_view.html',{'hosp':hosp})

def prescription(request,id):
    appointment_id=Appointment.objects.get(id=id)

    if request.method=='POST':
        form1=PrescriptionForm(request.POST,instance=appointment_id)
        if form1.is_valid():

            a=form1.save()
            a.Appointment_status=2
            a.save()
            
            return redirect('doctor_view')
    else:
          form1=PrescriptionForm(instance=appointment_id)
    return render(request,'prescription.html',{'form1':form1})



def prescription_view(request):
    loginid=request.session.get('doctor_id')
    doc=Doctor.objects.get(loginid=loginid)
    hosp = Appointment.objects.filter(doctor_id=doc)
    return render(request,'prescription_view.html',{'hosp':hosp})


def prescription_edit(request,id):
    appointment_id=Appointment.objects.get(id=id)
    if request.method=='POST':
        form1=PrescriptionForm(request.POST,instance=appointment_id)
        if form1.is_valid():
            b=form1.save(commit=False)
            b.save()
            return redirect('prescription_view')
    else:
          form1=PrescriptionForm(instance=appointment_id)
    return render(request,'prescription_edit.html',{'form1':form1})


def prescription_delete(request,id):
    data=Appointment.objects.get(id=id)
    data.delete()
    return redirect('prescription_view')


def complaint(request):
    loginid=request.session.get('user_id')
    user=Login.objects.get(id=loginid)
    if request.method=='POST':
        form1=ComplaintForm(request.POST)
        if form1.is_valid():
            b=form1.save(commit=False)
            b.loginid=user
            b.save()
            return redirect('complaint_view')
    else:
          form1=ComplaintForm()
    return render(request,'complaint.html',{'form1':form1})


def complaint_view(request):
    loginid=request.session.get('user_id')
    user=Login.objects.get(id=loginid)
    hosp = Complaint.objects.filter(loginid=user)
    return render(request,'complaint_view.html',{'hosp':hosp})


def complaint_edit(request,id):
    appointment_id=Complaint.objects.get(id=id)
    if request.method=='POST':
        form1=ComplaintForm(request.POST,instance=appointment_id)
        if form1.is_valid():
            b=form1.save(commit=False)
            b.save()
            return redirect('complaint_view')
    else:
          form1=ComplaintForm(instance=appointment_id)
    return render(request,'complaint_edit.html',{'form1':form1})

def complaint_delete(request,id):
    data=Complaint.objects.get(id=id)
    data.delete()
    return redirect('complaint_view')


def admin_complaintview(request):
    hosp = Complaint.objects.all()
    return render(request,'admin_complaintview.html',{'hosp':hosp})


def reply(request,id):
    complaint_id=Complaint.objects.get(id=id)

    if request.method=='POST':
        form1=ReplyForm(request.POST,instance=complaint_id)
        if form1.is_valid():
            form1.save()
            
            return redirect('admin_complaintview')
    else:
          form1=ReplyForm(instance=complaint_id)
    return render(request,'reply.html',{'form1':form1})


def product(request):
    
    if request.method=='POST':
        form1=ProductForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            
            return redirect('adminheader')
    else:
          form1=ProductForm()
    return render(request,'product.html',{'form1':form1})


def product_view(request):
    hosp = Product.objects.all()
    return render(request,'product_view.html',{'hosp':hosp})


def product_edit(request,id):
    data=Product.objects.get(id=id)
    
    if request.method=='POST':
        form1=ProductForm(request.POST,request.FILES,instance=data)
        if form1.is_valid():
            form1.save()
            
            return redirect('product_view')
    else:
          form1=ProductForm(instance=data)
    return render(request,'product_edit.html',{'form1':form1})


def product_delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('product_view')


def admin_docview(request):
    user=Doctor.objects.all()
    return render(request,'admin_docview.html',{'doc':user})


def admin_userview(request):
    user=User.objects.all()
    return render(request,'admin_userview.html',{'doc':user})


def user_productview(request):
    query=request.GET.get('q')
    if query: 
        serach=Product.objects.filter(
        Q(name__icontains=query)
        )
    else:
        search=Product.objects.all()
    return render(request,'user_productview.html',{'search':search,'query':query})  



def payment(request,id):
    product_id=Product.objects.get(id=id)

    loginid=request.session.get('user_id')
    user=User.objects.get(id=loginid)
    if request.method=='POST':
        form1=PaymentForm(request.POST)
        if form1.is_valid():
            b=form1.save(commit=False)
            b.product_id=product_id
            b.loginid=user
            b.save()
            return redirect('user_productview')
    else:
          form1=PaymentForm()
    return render(request,'payment.html',{'form1':form1})


def logout(request):
    request.session.flush()
    return redirect('login')

# def Search(request):
#     query=request.GET.get('q')
#     if query: 
#         serach=Product.objects.filter(
#         Q(name__icontains=query)
#         )
#     else:
#         search=Product.objects.all()
#     return render(request,'a.html',{'search':search,'query':query})        
