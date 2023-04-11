from django.shortcuts import render,redirect
from .models import *
from django.views.generic import TemplateView

def lugat(request):
  qidirish=request.GET.get('qidiruv_sozi')
  # if qidirish != '':
  togri_vari=Togri_soz.objects.filter(soz=qidirish)
  if len(togri_vari)==1:
    notogri_vari=Xato_soz.objects.filter(soz=togri_vari[0])
  else:
    notogri_vari=Xato_soz.objects.filter(xato=qidirish)
    if len(notogri_vari)==1:
      togri_vari=Togri_soz.objects.filter(id=notogri_vari[0].soz.id)
    else:
      # return redirect('result')
      pass
    
  data={
    'togri':togri_vari,
    'notogri':notogri_vari,
  }
  return render(request,'result.html',data)