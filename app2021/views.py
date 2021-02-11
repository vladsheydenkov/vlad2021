from django.shortcuts import render
from django.shortcuts import redirect
import json
from . import forms
from .models import Storage


def main(request):
    if request.method == 'POST':
        form = forms.InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['name']
            name = json.dumps(cd, ensure_ascii=False)
            new_entry = Storage(name=name)
            new_entry.save()
            return redirect('/')
    else:
        try:
            num_of_the_latest_material = Storage.objects.latest('id')
            counter = num_of_the_latest_material.id
        except:
            counter = ''
        form = forms.InputForm()
        return render(request,
                      'main.html',
                      {'form': form, 'num_of_the_latest_materaial': counter},
                      )


def all_materials(request):
    materials = Storage.objects.all()
    return render(request,
                  'all_materials.html',
                  {'materials': materials})
