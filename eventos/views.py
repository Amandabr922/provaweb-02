from django.shortcuts import render, redirect
from .forms import EventoForm

eventos_lista = [
    {"evento": "Seminário de estatística", "local": "Laboratório 01"},
    {"evento": "Semana da TI", "local": "Auditório"}
]

def home(request):
    return render(request, 'home.html', {'eventos': eventos_lista})


def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            eventos_lista.append({
                'evento': form.cleaned_data['evento'],
                'local': form.cleaned_data['local']
            })
            return redirect('home')
    else:
        form = EventoForm()

    return render(request, 'novo.html', {'form': form})