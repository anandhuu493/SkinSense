from django import forms
from .models import *






SKIN_TYPES = [
    ('oily', 'Oily'),
    ('dry', 'Dry'),
    ('combination', 'Combination'),
    ('normal', 'Normal'),
    ('sensitive', 'Sensitive'),
]

SKIN_TONES = [
    ('fair', 'Fair'),
    ('medium', 'Medium'),
    ('olive', 'Olive'),
    ('dark', 'Dark'),
]

SENSITIVITY_LEVELS = [
    ('low', 'Low'),
    ('moderate', 'Moderate'),
    ('high', 'High'),
]


GENDER_CHOICES = [
    ('MALE', 'MALE'),
    ('F', 'FEMALE'),
    ('OTHER', 'OTHER'),

]
class UserForm(forms.ModelForm):
    name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        })
    )
    contact = forms.CharField(
        label="Contact",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'contact number',
        })
    )
    skintone = forms.ChoiceField(
        choices=SKIN_TONES,
        label="Skin Tone",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    skintype = forms.ChoiceField(
        choices=SKIN_TYPES,
        label="Skin Type",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sensitivity_level = forms.ChoiceField(
        choices=SENSITIVITY_LEVELS,
        label="Sensitivity Level",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['name', 'contact', 'skintone', 'skintype', 'sensitivity_level',]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']
        widgets={
            'email':forms.EmailInput(attrs={'type':'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label="Gender",
        widget=forms.RadioSelect()
    )
    class Meta:
        model = Doctor
        fields = ['name','hospitalid','gender','dob','qualifications','experience','contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'hospitalid': forms.Select(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'qualifications': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['hospitalid'].empty_label = "Select Hospital"


class Customloginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['Hospital_name', 'Address', 'State', 'District', 'City']
        widgets = {
            'Hospital_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hospital name'}),
            'Address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'State': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'District': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter district'}),
            'City': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
        }
        
class Appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date','time']
        widgets={
            'date':forms.DateInput(attrs={'type':'date'}),
            'time':forms.TimeInput(attrs={'type':'time'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['prescription']
        widgets = {
            'prescription': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter prescription here...',
                'rows': 5,
                'style': 'resize: vertical; border-radius: 8px; padding: 10px; font-size: 16px;'
            }),
        }
        labels = {
            'prescription': 'Prescription Notes',
        }



class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['reply']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['account_holder_name','card_number','cvv','expiry_date']


