from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()

    return render(
        request,
        'usuarios/registro.html',
        {
            'form': form
        }
    )

@login_required
def bienvenida(request):
    return render(
        request,
        'usuarios/bienvenida.html'
    )

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('bienvenida')
    else:
        form = EditarUsuarioForm(
            instance=request.user
        )

    return render(
        request,
        'usuarios/editar_perfil.html',
        {
            'form': form
        }
    )
