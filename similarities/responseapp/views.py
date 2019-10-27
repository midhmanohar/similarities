from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse


def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            resl = myForm.cleaned_data['resl']

            context = {
            'name': name,
            'resl': resl
            }

            template = loader.get_template('thankyou.html')

            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()

     return render(request, 'responseform.html', {'form':form});
