from django.http import HttpResponse
from django.template import loader
from .models import Membro

def membros(request):
    meus_membros = Membro.objects.all().values()
    template = loader.get_template('todos_membros.html')
    context = {
        'meus_membros': meus_membros,
    }

    return HttpResponse(template.render(context, request))

def detalhes(request, membro_id):
    membro = Membro.objects.get(id=membro_id)
    template = loader.get_template('detalhes.html')
    context = {
        'meu_membro': membro,
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
  meus_membros = Membro.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'meus_membros': meus_membros, 
  }
  return HttpResponse(template.render(context, request))
