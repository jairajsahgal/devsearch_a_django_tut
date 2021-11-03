from django.contrib import admin
from .models import Project, Review, Tag
# Help us activate our admin panel.
# Register your models here.

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)