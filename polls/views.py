from http.client import HTTPResponse
from django.db.models import F

from django.core.mail import EmailMessage

from django.template.loader import render_to_string

from xhtml2pdf import pisa

from django.template import loader

from django.core.mail import send_mail

from io import BytesIO

from .models import Turno
from .forms import TurnoForm

from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt



# Vista principal (lista de preguntas)
def index(request):
    context = {
        'mensaje': 'Bienvenid@ a Raíces del Alma'
    }
    return render(request, 'polls/index.html', context)

def masaje_facial(request):
    return render(request, 'polls/masaje_facial.html')

def masaje_relajante(request):
    return render(request, 'polls/masaje_relajante.html')

def masaje_descontracturante(request):
    return render(request, 'polls/masaje_descontracturante.html')

def turno_forms(request):
    if request.method == 'POST':
        if request.POST.get('accion') == 'cancelar':
            return redirect('polls:index')  # o a donde quieras volver

        form = TurnoForm(request.POST)
        if form.is_valid():
            turno = form.save()
            return render(request, 'polls/confirmacion_pdf.html', {'turno': turno})
    else:
        form = TurnoForm()

    return render(request, 'polls/tomar_turno.html', {'form': form})

def cancelar_turno(request, turno_id):
    turno = get_object_or_404(Turno, pk=turno_id)
    
    if request.method == 'POST':
        turno.delete()
        return redirect('polls:index')  # O a donde quieras redirigir después

    return redirect('polls:tomar_turno')  # Por si se accede por GET

def lista_turnos(request):
    turnos = Turno.objects.all().order_by('fecha')
    return render(request, 'polls/lista_turnos.html', {'turnos': turnos})

def enviar_mail_demo(request):
    send_mail(
        'Asunto del correo',
        'Este es el mensaje de prueba.',
        'noreply@ejemplo.com',
        ['usuario@correo.com'],
        fail_silently=False,
    )
    return HTTPResponse("Correo enviado (ver consola).") 
@csrf_exempt  # solo si estás probando y querés simplificar; en producción usá POST + csrf_token
def limpiar_turnos(request):
    if request.method == 'POST':
        Turno.objects.all().delete()
        return redirect('polls:lista_turnos')  # o donde quieras redirigir








