from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    data = {'title' :'Help Page'}
    return render(request, 'AppTwo/help.html', context=data)

def users(request):
#    users = User.objects.order_by('email')
#    user_dict = {'user_records' : users}
#    return render(request, 'AppTwo/users.html', context=user_dict)
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'AppTwo/users.html', {'form': form})
