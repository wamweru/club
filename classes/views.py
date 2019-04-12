from django.shortcuts import render, get_object_or_404,redirect
from .models import Club, Student
from .forms import ClubForm,StudentForm, UserForm
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
# Create your views here.


@login_required(login_url='classes:login')
def index(request):
    clubs = Club.objects.all()
    student_results = Student.objects.all()
    query = request.GET.get("q")
    if query:
        clubs = clubs.filter(
            Q(club_name__icontains=query)

        ).distinct()
        student_results = student_results.filter(
            Q(student_name__icontains=query)
        ).distinct()
        return render(request, 'classes/index.html', {
            'clubs': clubs,
            'student': student_results,
        })
    return render(request, 'classes/index.html', {'clubs': clubs})


def detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)

    return render(request, 'classes/detail.html', {'club': club})

def create_club(request):
    form = ClubForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        club = form.save(commit=False)
        club.club_logo = request.FILES['club_logo']
        club.save()
        return render(request, 'classes/detail.html',{'club':club})
    return render(request, 'classes/create_club.html',{'form':form})

def create_student(request, club_id):
    form = StudentForm(request.POST or None, request.FILES or None)
    club = get_object_or_404(Club, pk=club_id)
    if form.is_valid():
        student = form.save(commit=False)
        student.club = club
        student.cover = request.FILES['cover']
        student.save()
        return render(request, 'classes/detail.html', {'club': club})
    return render(request, 'classes/create_student.html',{'form':form})

def delete_club(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    club.delete()
    return redirect('/')


class ClubUpdateView(UpdateView):
        model = Club
        fields = ['club_name', 'club_logo']
        template_name = 'classes/create_club.html'


def delete_student(request, club_id, student_id):
    club = get_object_or_404(Club, pk=club_id)
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    context = {
        'club': club,
        'message': 'Member Deleted Successfully'

    }
    return render(request, 'classes/detail.html', context)


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['student_name', 'student_age', 'stream', 'cover']
    template_name = 'classes/create_student.html'


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('classes:index')

    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)

    return redirect('classes:login')

def signup(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:

                return redirect('classes:index')
    return render(request, 'registration/signup.html', {'form': form})

