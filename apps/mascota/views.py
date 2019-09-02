from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota


# Create your views here.

def listadousuarios(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
    return HttpResponse(lista, content_type='application/json')


def index(request):
    return render(request, 'mascota/index.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    # paginate_by = 5


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

    def get_context_data(self, **kwargs):
        context = super(MascotaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

    def get_context_data(self, **kwargs):
        context = super(MascotaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        mascota = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class(instance=mascota)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_mascota = kwargs['pk']
        mascota = self.model.objects.get(id=id_mascota)
        form = self.form_class(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')
