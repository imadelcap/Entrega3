from django.http import HttpResponse
from django.template import loader


def pagina_base(request):
    plantilla = loader.get_template("base.html")
    documento = plantilla.render()
    return HttpResponse(documento)

