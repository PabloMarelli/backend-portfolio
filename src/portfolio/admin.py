from django.contrib import admin

from portfolio.models import (
    Resumee,
    Experience,
    Contact
)



admin.site.register(Resumee)
admin.site.register(Experience)
admin.site.register(Contact)
