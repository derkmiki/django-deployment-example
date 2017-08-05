from django.shortcuts import render
from AppTwo.models import User

# Create your views here.
def users(request):
    user_list = User.objects.order_by('email')
    user_dict = {'users' : user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)
