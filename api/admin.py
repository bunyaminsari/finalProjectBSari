from django.contrib import admin


from .models import Query, Profile

admin.site.register(Query)
admin.site.register(Profile)