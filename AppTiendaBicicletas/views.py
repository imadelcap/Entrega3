from django.shortcuts import render
from AppTiendaBicicletas.models import ModeloBicicleta, Accesorio, Cliente
from AppTiendaBicicletas.forms import ClienteFormulario, AccesorioFormulario, ModeloBicicletaFormulario

def inicio(request):
    return render(request, 'index.html')

def formulario_modelo_bicicleta(request):
    if request.method == 'POST':
        #modelo_bicicleta = ModeloBicicleta(request.POST['marca'], request.POST['tipo'], request.POST['rodado'])
        modelo_bicicleta = ModeloBicicleta(marca = request.POST['marca'], tipo = request.POST['tipo'], rodado = request.POST['rodado'])
        modelo_bicicleta.save()
        return render(request, 'index.html')    
    
    return render(request, 'formulario_modelo_bicicleta.html')

def formulario_modelo_bicicleta1(request): # con este metodo no me generaba el objeto formulario, solo me aparecia el boto de submit. Por eso le cambie el nombre a la funcion. Luego corregi el segundo return y aplique los cambios a los otros formularios
    if request.method == 'POST':
        formulario = ModeloBicicletaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_bicicleta = ModeloBicicleta(datos['marca'], datos['tipo'], datos['rodado'])
            modelo_bicicleta.save()
            return render(request, 'inicio.html')    
    
    
    formulario = ModeloBicicletaFormulario(request.POST)
    #return render(request, 'formulario_modelo_bicicleta.html')
    return render(request, 'formulario_modelo_bicicleta.html', { 'formulario': formulario })

def formulario_cliente(request):
    if request.method == 'POST':
        formulario = ClienteFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            #cliente = Cliente(datos['nombre'], datos['apellido'], datos['email'], datos['edad'])
            cliente = Cliente(nombre = datos['nombre'], apellido = datos['apellido'], email = datos['email'], edad = datos['edad'])
            cliente.save()
            return render(request, 'index.html')    
    
    formulario = ClienteFormulario(request.POST)
    return render(request, 'formulario_cliente.html',  {'formulario': formulario })

def formulario_accesorio(request):
    if request.method == 'POST':
        formulario = AccesorioFormulario(request.POST)
     

        if formulario.is_valid():
            datos = formulario.cleaned_data
            #print(datos) #Para debugging#
            #accesorio = Accesorio(datos["tipo"], datos["marca"], datos["descripcion"])
            accesorio = Accesorio(tipo = datos["tipo"], marca = datos["marca"], descripcion = datos["descripcion"])
            
            #print(accesorio) #Para debugging#
            accesorio.save()
            return render(request, 'index.html')

    
    formulario = AccesorioFormulario(request.POST)
    return render(request, 'formulario_accesorio.html', {'formulario': formulario })


def buscar_cliente(request):
    return render(request, 'formulario_buscar_cliente.html')

def buscar_accesorio(request):
    return render(request, 'formulario_buscar_accesorio.html')

def buscar_modelo_bicicleta(request):
    return render(request, 'formulario_buscar_modelo_bicicleta.html')