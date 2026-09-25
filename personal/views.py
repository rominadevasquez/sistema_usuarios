from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Empleado
from .forms import EmpleadoForm


@login_required
def inicio_personal(request):
    return render(
        request,
        'personal/inicio.html'
    )


@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()

    return render(
        request,
        'personal/lista_empleados.html',
        {
            'empleados': empleados
        }
    )


@login_required
def crear_empleado(request):

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_empleados')

    else:
        form = EmpleadoForm()

    return render(
        request,
        'personal/crear_empleado.html',
        {
            'form': form
        }
    )


@login_required
def detalle_empleado(request, empleado_id):

    empleado = get_object_or_404(
        Empleado,
        id=empleado_id
    )

    return render(
        request,
        'personal/detalle_empleado.html',
        {
            'empleado': empleado
        }
    )


@login_required
def editar_empleado(request, empleado_id):

    empleado = get_object_or_404(
        Empleado,
        id=empleado_id
    )

    if request.method == 'POST':

        form = EmpleadoForm(
            request.POST,
            instance=empleado
        )

        if form.is_valid():
            form.save()
            return redirect('lista_empleados')

    else:

        form = EmpleadoForm(
            instance=empleado
        )

    return render(
        request,
        'personal/editar_empleado.html',
        {
            'form': form,
            'empleado': empleado
        }
    )


@login_required
def eliminar_empleado(request, empleado_id):

    empleado = get_object_or_404(
        Empleado,
        id=empleado_id
    )

    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')

    return render(
        request,
        'personal/eliminar_empleado.html',
        {
            'empleado': empleado
        }
    )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Empleado
from .forms import EmpleadoForm


@login_required
def inicio_personal(request):
    return render(
        request,
        'personal/inicio.html'
    )


@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()

    return render(
        request,
        'personal/lista_empleados.html',
        {
            'empleados': empleados
        }
    )


@login_required
def crear_empleado(request):

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_empleados')

    else:
        form = EmpleadoForm()

    return render(
        request,
        'personal/crear_empleado.html',
        {
            'form': form
        }
    )


@login_required
def detalle_empleado(request, empleado_id):

    empleado = get_object_or_404(
        Empleado,
        id=empleado_id
    )

    return render(
        request,
        'personal/detalle_empleado.html',
        {
            'empleado': empleado
        }
    )


@login_required
def editar_empleado(request, empleado_id):

    empleado = get_object_or_404(
        Empleado,
        id=empleado_id
    )

    if request.method == 'POST':

        form = EmpleadoForm(
            request.POST,
            instance=empleado
        )

        if form.is_valid():
            form.save()
            return redirect('lista_empleados')

    else:

        form = EmpleadoForm(
            instance=empleado
        )

    return render(
        request,
        'personal/editar_empleado.html',
        {
            'form': form,
            'empleado': empleado
        }
    )


@login_required
def eliminar_empleado(request, empleado_id):

    empleado = get_object_or_404(
        Empleado,
        id=empleado_id
    )

    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')

    return render(
        request,
        'personal/eliminar_empleado.html',
        {
            'empleado': empleado
        }
    )

