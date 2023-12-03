from django.shortcuts import render
from AppTiendaBicicletas.models import ModeloBicicleta, Accesorio, Cliente
from AppTiendaBicicletas.forms import ClienteFormulario, AccesorioFormulario, ModeloBicicletaFormulario

def inicio(request):
    return render(request, 'index.html')

def formulario_modelo_bicicleta(request):
    if request.method == 'POST':
        modelo_bicicleta = ModeloBicicleta(request.POST['marca'], request.POST['tipo'], request.POST['rodado'])
        modelo_bicicleta.save()
        return render(request, 'inicio.html')    
    
    return render(request, 'formulario_modelo_bicicleta.html')

def formulario_modelo_bicicleta1(request): # con este metodo no me generaba el objeto formulario, solo me aparecia el boto de submit. Por eso le cambie el nombre a la funcion
    if request.method == 'POST':
        formulario = ModeloBicicletaFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_bicicleta = ModeloBicicleta(datos['marca'], datos['tipo'], datos['rodado'])
            modelo_bicicleta.save()
            return render(request, 'inicio.html')    
    
    
    formulario = ModeloBicicletaFormulario(request.POST)
    return render(request, 'formulario_modelo_bicicleta.html', { 'formulario': formulario })

def formulario_cliente(request):
    if request.method == 'POST':
        formulario = ClienteFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            cliente = Cliente(datos['nombre'], datos['apellido'], datos['email'], datos['edad'])
            cliente.save()
            return render(request, 'inicio.html')    
    
    formulario = ClienteFormulario(request.POST)
    return render(request, 'formulario_cliente.html',  {'formulario': formulario })

def formulario_accesorio(request):
    if request.method == 'POST':
        formulario = AccesorioFormulario(request.POST)
        print(formulario)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            accesorio = Accesorio(datos['tipo'], datos['marca'], datos['descripcion'])
            accesorio.save()
            return render(request, 'inicio.html')

    
    formulario = AccesorioFormulario(request.POST)
    return render(request, 'formulario_accesorio.html', {'formulario': formulario })

