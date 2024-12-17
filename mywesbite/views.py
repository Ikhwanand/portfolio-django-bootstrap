from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Experience, Education, Skill, ProgrammingSkill, Project, Contact
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(f"Form submitted: {form.is_valid()}")
        if form.is_valid():
            # If the form is valid, save
            form.save()
            # Display a success message
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('mywesbite:contact')
        else:
            # if the form is not valid, display an error message
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    programmingskills = ProgrammingSkill.objects.all()
    return render(request, 'resume.html', {'experiences': experiences, 'educations': educations, 'skills': skills, 'programmingskills': programmingskills})
