from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Marriage_Certificate_Form,ProjectForm,ProfileForm,UserForm
from .models import Document,Project,Profile
from .field_option import Options
from django.http import HttpResponseRedirect
import re
from django.contrib.auth.models import User
import pandas as pd
# Create your views here.
def testuser(request):
    form = UserForm
    project_list = Project.objects.all()
    return render(request, 'document/test.html', {'project_list':project_list, 'form':form})

def user(request):
    

    form = UserForm
    project_list = Project.objects.all()
    return render(request, 'document/user.html', {'project_list':project_list, 'form':form})

def project(request):
    submitted = False
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form= ProjectForm
            if 'submitted' in request.GET:
                submitted = True
    
    form = ProjectForm
    project_list = Project.objects.all()
    return render(request, 'document/project.html', {'project_list':project_list, 'form':form, 'submitted':submitted})


def insert_data(request):   
    if request.method == 'POST':
        if 'save_data' in request.POST:
            document_name = request.POST.get("save_data")
            print(document_name)
            current_document = Document.objects.filter(document_name = document_name)
            if current_document.exists():
                current_document = Document.objects.get(document_name = document_name)
                form = Marriage_Certificate_Form(request.POST)
                form_instance = form.save(commit=False)
                form_instance.document = current_document
                form_instance.insert_user = request.user
                form_instance.save()
                if form.is_valid():
                    form.save_m2m()
                    messages.success(request,('Data has Been Uploaded'))
                else:
                    messages.success(request,('Document not exist in database')) 
            return redirect('insert')

    else:
        mcForm = Marriage_Certificate_Form()
        documents = Document.objects.filter(user = request.user, insert_status ='new')
        if documents.exists():
            current_document = documents[0].document_name
        else:
           current_document = 0
    return render(request,'document/insert.html',{'forms' : mcForm, 'documents': documents, 'current_document': current_document})


def insert_user(request):
    if request.POST:
        if 'filename' in request.FILES:
            uploaded_file = request.FILES['filename']
            allowed_extensions = ['xls', 'xlsm', 'xlsx', 'xlt']
            if uploaded_file.name.split('.')[-1] in allowed_extensions:
                df = pd.read_excel(uploaded_file, header=0)
                for index, row in df.iterrows():
                    try:
                        current_user = User.objects.get(
                            username=row['username'])
                    except User.DoesNotExist:
                        current_project = Project.objects.filter(
                            project_name=row['project_name'])
                        if current_project.exists():
                            password = str(row['password'])
                            user = User.objects.create_user(
                                username=row['username'],
                                password=password
                            )
                            current_project = Project.objects.get(
                            project_name=row['project_name'])
                            profile_instance = User_Profile.save(commit=False)
                            profile_instance.user = user
                            profile_instance.project = current_project
                            profile_instance.description = row['description']
                            profile_instance.user_type = row['user_type']
                            profile_instance.save()
                return redirect('profile')

        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                current_user = User.objects.get(username=username)
                messages.error(request, 'User already exists')
                return redirect('profile')
            except User.DoesNotExist:
                User_Profile = ProfileForm(request.POST)
                if User_Profile.is_valid():
                    user = User.objects.create_user(
                        username=username,
                        password=password
                    )
                    profile_instance = User_Profile.save(commit=False)
                    profile_instance.user = user
                    profile_instance.save()
                    messages.success(request, 'User has been created')
                    return redirect('profile')
    else:
        User_Profile = ProfileForm()
        projects = Project.objects.all()
        users = Profile.objects.all()
    return render(request, 'document/user.html', {'form': User_Profile, 'users': users, 'project_list': projects})

def login(request):
    return render(request,'auth/login.html')

def register(request):
    return render(request,'auth/register.html')