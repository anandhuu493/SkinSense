from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.landing,name='landing'),

    path('login',views.login,name='login'),
    path('admin',views.admin,name='admin'),
    path('about',views.about,name='about'),
    path('userregistration',views.userregistration,name='userregistration'),
    path('doctorregistration',views.doctorregistration,name='doctorregistration'),
    path('hospitalregistration',views.hospitalregistration,name='hospitalregistration'),
    path('userhome',views.userhome,name='userhome'),
    path('hospitalhome',views.hospitalhome,name='hospitalhome'),
    path('doctorhome',views.doctorhome,name='doctorhome'),
    path('user_edit',views.user_edit,name='user_edit'),
    path('doctor_edit',views.doctor_edit,name='doctor_edit'),
    path('hospital_edit',views.hospital_edit,name='hospital_edit'),
    path('adminhospital_list',views.adminhospital_list,name='adminhospital_list'),
    path('adminuser_list',views.adminuser_list,name='adminuser_list'),
    path('admindoctor_list',views.admindoctor_list,name='admindoctor_list'),
    path('adminheader',views.adminheader,name='adminheader'),
    path('userdoclist',views.userdoclist,name='userdoclist'),
    path('appointment/<int:did>',views.appointment,name='appointment'),
    path('appointment_list',views.appointment_list,name='appointment_list'),
    path('appointment_edit/<int:id>',views.appointment_edit,name='appointment_edit'),
    path('appointment_delete/<int:id>',views.appointment_delete,name='appointment_delete'),
    path('doctor_view',views.doctor_view,name='doctor_view'),
    path('prescription/<int:id>',views.prescription,name='prescription'),
    path('prescription_view',views.prescription_view,name='prescription_view'),
    path('prescription_edit/<int:id>',views.prescription_edit,name='prescription_edit'),
    path('prescription_delete/<int:id>',views.prescription_delete,name='prescription_delete'),
    path('landingsubheader',views.landingsubheader,name='landingsubheader'),
    path('subheader',views.subheader,name='subheader'),
    path('doctorsubheader',views.doctorsubheader,name='doctorsubheader'),
    path('usersubheader',views.usersubheader,name='usersubheader'),
    path('hospitalsubheader',views.hospitalsubheader,name='hospitalsubheader'),
    path('complaint',views.complaint,name='complaint'),
    path('complaint_view',views.complaint_view,name='complaint_view'),
    path('complaint_edit/<int:id>',views.complaint_edit,name='complaint_edit'),
    path('complaint_delete/<int:id>',views.complaint_delete,name='complaint_delete'),
    path('admin_complaintview',views.admin_complaintview,name='admin_complaintview'),
    path('reply/<int:id>',views.reply,name='reply'),
    path('product',views.product,name='product'),
    path('product_view',views.product_view,name='product_view'),
    path('product_edit/<int:id>',views.product_edit,name='product_edit'),
    path('product_delete/<int:id>',views.product_delete,name='product_delete'),
    path('admin_docview',views.admin_docview,name='admin_docview'),
    path('admin_userview',views.admin_userview,name='admin_userview'),
    path('user_productview',views.user_productview,name='user_productview'),
    path('payment/<int:id>',views.payment,name='payment'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('doctor_approve<int:id>',views.doctor_approve,name='doctor_approve'),
    path('doctor_reject/<int:id>',views.doctor_reject,name='doctor_reject'),

    path('logout',views.logout,name='logout'),




    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)