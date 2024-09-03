from django.contrib import admin
from .models import Article, Jobs, Services, Order

admin.site.site_header = "Al-Gammal Admin"
admin.site.site_title = "Al-Gammal Admin"

admin.site.register(Article)
admin.site.register(Jobs)
admin.site.register(Services)
admin.site.register(Order)