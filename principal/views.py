from django.shortcuts import redirect, render
from .models import Persona
from principal.forms import PersonaForm


def home(request):
    personas = Persona.objects.all()
    contexto =  {
        "personas": personas
    }
    return render(request, "index.html", contexto)

def registro(request):
    if request.method == "POST":
        formulario = PersonaForm(request.POST)    
        
        if formulario.is_valid():
            formulario.save()
            return redirect("Home")
    else:
        formulario = PersonaForm()        

    return render(request, "registrar.html", {"formulario": formulario} )

def editar(request, id_persona):
    persona = Persona.objects.get(id_persona = id_persona)
    if request.method == "POST":
        formulario = PersonaForm(request.POST, instance = persona)
        if formulario.is_valid():
            formulario.save()
            return redirect("Home")
    else:
        formulario = PersonaForm(instance = persona)
       

    return render(request, "editar.html", {'formulario': formulario} )

def eliminar(request, id_persona):
    persona = Persona.objects.get(id_persona = id_persona)
    persona.delete()
    return redirect("Home")

#def registroLlamadoForm(request):
 #   if request.method == "POST":
  #      formulario = PersonaForm(request.POST)    
        
     #   if formulario.is_valid():
       #     formulario.save()
      #      return redirect("Home")
 #   else:
   #     formulario = PersonaForm()    
   # return render(request, "registrar_llamado_form.html", {"formulario": formulario} )