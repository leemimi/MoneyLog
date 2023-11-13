from django.shortcuts import render
from .models import MyAccount
def index(request):
    content_list = MyAccount.objects.all()
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

