import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker
f = Faker()
def populate(N=5):
    for i in range(N):
        fake_fn = f.first_name()
        fake_ln = f.last_name()
        fake_email = f.profile('email')['mail']
        User.objects.create(first_name=fake_fn, last_name=fake_ln, email=fake_email)


if __name__ == '__main__':
    print('populating!')
    populate(N=20)
    print('complete!')
