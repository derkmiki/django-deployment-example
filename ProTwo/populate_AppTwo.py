import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import User

def populate(N=5):
    for i in range(N):
        f = Faker()
        fake_first_name = f.first_name()
        fake_last_name = f.last_name()
        fake_email =  f.profile('email')['mail']
        User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('done populating script!')
