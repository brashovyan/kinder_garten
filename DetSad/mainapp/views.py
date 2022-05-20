from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Organization, Section, Child, Parent, Garten
from .forms import RegForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    else:
        if User.objects.filter(pk=request.user.id, groups__name='Parent').exists():
            parent = Parent.objects.get(person = request.user)
            childs = Child.objects.filter(parents = parent)
            return render(request, 'mainapp/parent_profile.html', {'person': request.user, 'childs':childs })

        elif User.objects.filter(pk=request.user.id, groups__name='Admin_organization').exists():
            return render(request, 'mainapp/parent_profile.html', {'person': request.user})

        elif User.objects.filter(pk=request.user.id, groups__name='Admin_garten').exists():
            return render(request, 'mainapp/parent_profile.html', {'person': request.user})

        else:
            return HttpResponseRedirect('/login')


def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            error = "Неверный логин или пароль! Проверьте раскладку языка. Также напоминаем, что буквы верхнего и нижнего регистра (строчные и заглавные) отличаются между собой."
            return render(request, 'mainapp/login.html', {'error': error})

    else:
        if request.user.is_authenticated:
            logout(request)
        return render(request, 'mainapp/login.html')


def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                try:
                    user = User.objects.create_user(username, email, password1)
                except:
                    error = "Данный логин уже занят. Попробуйте другой."
                    form = RegForm()
                    return render(request, 'mainapp/register.html', {'form': form, 'error': error})
                if request.user.is_authenticated:
                    logout(request)
                login(request, user)

                user2 = User.objects.get(username=request.user.username)
                group = Group.objects.get(name='Parent')
                user2.groups.add(group)
                Parent.objects.create(person=request.user)
                return HttpResponseRedirect("/")
            else:
                error = "Пароли не совпадают!"
                form = RegForm()
                return render(request, 'mainapp/register.html', {'form': form, 'error':error})

        else:
            error = "Вы ввели некорректные данные! Повторите попытку, заполнив все поля по подсказкам."
            return render(request, 'mainapp/register.html', {'form': form, 'error': error})
    else:
        form = RegForm()
        return render(request, 'mainapp/register.html', {'form': form})


def change_profile(request, id):
    user = User.objects.get(id=id)
    if user == request.user:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            if first_name != '':
                user.first_name = first_name
            if last_name != '':
                user.last_name = last_name
            user.save()

            return HttpResponseRedirect('/')

        else:
            return render(request, 'mainapp/change_profile.html', {'person': user})
    else:
        return HttpResponseRedirect('/')


def logout1(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def child_info(request, id):
    parent = Parent.objects.get(person=request.user)
    childs = Child.objects.filter(parents=parent)
    child = Child.objects.get(id=id)
    sections = child.sections.all()
    s = float(0)
    for section in sections:
        s += float(section.load)
    if child in childs:
        return render(request, 'mainapp/child_info.html', {'child':child, 'load':s})
    else:
        return HttpResponseRedirect('/')


def add_section_child(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                c = request.POST['selected_child']
                child = Child.objects.get(id=c)
                s = request.POST['selected_section']
                section = Section.objects.get(id=s)
                child.sections.add(section)
                return HttpResponseRedirect('/')

            except:
                parent = Parent.objects.get(person=request.user)
                childs = Child.objects.filter(parents=parent)
                sections = Section.objects.all()
                error = "Произошла ошибка!"
                return render(request, 'mainapp/add_section_child.html', {'childs': childs, 'sections': sections, 'error':error})

        else:
            parent = Parent.objects.get(person=request.user)
            childs = Child.objects.filter(parents=parent)
            sections = Section.objects.all()
            return render(request, 'mainapp/add_section_child.html', {'childs':childs, 'sections':sections})
    else:
        return HttpResponseRedirect('/login')


def sections(request):
    if request.user.is_authenticated:
        sections = Section.objects.all()
        return render(request, 'mainapp/sections.html', {'sections': sections})
    else:
        return HttpResponseRedirect('/login')






