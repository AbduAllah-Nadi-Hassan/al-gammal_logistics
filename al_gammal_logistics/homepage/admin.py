from django.contrib import admin
from .models import Article, Jobs, Services

admin.site.site_header = "Al-Gammal Admin"
admin.site.site_title = "Al-Gammal Admin"

admin.site.register(Article)
admin.site.register(Jobs)
admin.site.register(Services)