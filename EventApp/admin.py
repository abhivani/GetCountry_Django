from django.contrib import admin
from EventApp.models import user_data, Person

# Register your models here.


admin.site.register(user_data)


admin.site.register(Person)