from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.decorators.http import require_GET

from .forms import TaskForm, SolicitudForm, SignUpForm, LoginForm
from .models import Task, Solicitud, Categoria, Subcategoria, Respuesta
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, 'home.html')

def signup(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('dashboard_admin')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'msg': msg})


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks' : tasks})
@login_required
def respuestas(request):
    respuestas = Respuesta.objects.filter()
    return render(request, 'respuestas.html', {'respuestas' : respuestas})
def dashboard_admin(request):
    tasks = Task.objects.filter()
    categorias = Categoria.objects.filter()
    subcategorias = Subcategoria.objects.filter()
    solicitudes = Solicitud.objects.filter()
    users = User.objects.filter()
    return render(request, 'dashboard_admin.html', {'tasks' : tasks,
                                                    'categorias': categorias,
                                                    'subcategorias': subcategorias,
                                                    'solicitudes': solicitudes,
                                                    'users': users
                                                    })

def list_tasks(_request):
    tasks = list(Task.objects.values())
    data = {'tasks' : tasks}
    return JsonResponse(data)

def list_usuarios(_request):
    users = list(User.objects.values())
    data = {'users' : users}
    return JsonResponse(data)

def dashboard_ejecutivo(request):
    tasks = Task.objects.filter()
    categorias = Categoria.objects.filter()
    subcategorias = Subcategoria.objects.filter()
    solicitudes = Solicitud.objects.filter()
    users = User.objects.filter()
    return render(request, 'dashboard_ejecutivo.html', {'tasks' : tasks,
                                                    'categorias': categorias,
                                                    'subcategorias': subcategorias,
                                                    'solicitudes': solicitudes,
                                                    'users': users
                                                    })

def dashboard_cliente(request):
    tasks = Task.objects.filter()
    categorias = Categoria.objects.filter()
    subcategorias = Subcategoria.objects.filter()
    solicitudes = Solicitud.objects.filter(user=request.user)
    users = User.objects.filter()
    return render(request, 'dashboard_cliente.html', {'tasks' : tasks,
                                                    'categorias': categorias,
                                                    'subcategorias': subcategorias,
                                                    'solicitudes': solicitudes,
                                                    'users': users
                                                    })

@login_required
def solicitudes(request):
    solicitudes = Solicitud.objects.filter(user=request.user)
    return render(request, 'solicitudes.html', {'solicitudes' : solicitudes})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks' : tasks})

@login_required
def solicitudes_completed(request):
    solicitudes = Solicitud.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'solicitudes.html', {'solicitudes' : solicitudes})

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        respuesta = task.respuesta_set.first()
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'respuesta': respuesta, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            respuesta = Respuesta.objects.filter()
            form = TaskForm(request.POST, instance=task)

            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'respuesta': respuesta, 'form': form, 'error': "Error updating task"})

@login_required
def solicitud_detail(request, solicitud_id):
    if request.method == 'GET':
        solicitud = get_object_or_404(Solicitud, pk=solicitud_id, user=request.user)
        form = SolicitudForm(instance=solicitud)
        return render(request, 'solicitud_detail.html', {'solicitud': solicitud, 'form': form})
    else:
        try:
            solicitud = get_object_or_404(Solicitud, pk=solicitud_id, user=request.user)
            form = SolicitudForm(request.POST, instance=solicitud)
            form.save()
            return redirect('solicitudes')
        except ValueError:
            return render(request, 'solicitud_detail.html', {'solicitud': solicitud, 'form': form, 'error': "Error updating task"})
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('dashboard_admin')

@login_required
def complete_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud,pk=solicitud_id, user=request.user)
    if request.method == 'POST':
        solicitud.datecompleted = timezone.now()
        solicitud.save()
        return redirect('dashboard_admin')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard_admin')


@login_required
def delete_solicitud(request,solicitud_id):
    solicitud = get_object_or_404(Solicitud,pk=solicitud_id, user=request.user)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('dashboard_admin')

@login_required
def create_task(request):
    if request.method =='GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('dashboard_admin')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error' : ' Please provide valide data'
            })

@login_required
def create_solicitud(request):
    if request.method =='GET':
        return render(request, 'create_solicitud.html', {
            'form': SolicitudForm
        })
    else:
        try:
            form = SolicitudForm(request.POST)
            new_solicitud = form.save(commit=False)
            new_solicitud.user = request.user
            new_solicitud.save()
            user = request.user
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard_admin')
            elif user is not None and user.is_ejecutivo:
                login(request, user)
                return redirect('dashboard_ejecutivo')
            elif user is not None and user.is_cliente:
                login(request, user)
                return redirect('dashboard_cliente')
        except ValueError:
            return render(request, 'create_solicitud.html', {
                'form': SolicitudForm,
                'error' : ' Please provide valide data'
            })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('dashboard_admin')
        elif user is not None and user.is_ejecutivo:
            login(request, user)
            return redirect('dashboard_ejecutivo')
        elif user is not None and user.is_cliente:
            login(request, user)
            return redirect('dashboard_cliente')
        else:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña invalidos'
            })

def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': SignUpForm(request.POST)
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(email=request.POST['email'],
                                                password=request.POST['password1'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                mobile=request.POST['mobile'],
                                                )
                user.save()
                login(request, user)
                return redirect('dashboard_admin')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': SignUpForm(request.POST),
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': SignUpForm(request.POST),
            "error": 'La contraseña no es correcta'
        })

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg':msg})

@require_GET
def subcategorias_por_categoria(request):
    categoria_id = request.GET.get('categoria_id')

    subcategorias = Subcategoria.objects.filter(categoria_id=categoria_id)
    subcategorias_data = [{'id': sc.id, 'title': sc.title} for sc in subcategorias]

    return JsonResponse({'subcategorias': subcategorias_data})
