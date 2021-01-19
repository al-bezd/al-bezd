from django.shortcuts import render
from .models import send as send_email
from django.views.generic import TemplateView




def send(request):
    _ = request.GET
    context = {
        'success_reciver':[],
        'err_reciver':[]
    }
    context.update(_.dict())
    for i in _['emails'].split('\r\n'):
        i = i.replace(' ','')
        result = send_email(_['subject'],_['login'],_['password'],i,_['msg'])
        if result == 'ok':
            context['success_reciver'].append(i)
        else:
            context['err_reciver'].append({'err':f'{result}','text':i})

    return render(request, 'message_sender\index.html', context)
