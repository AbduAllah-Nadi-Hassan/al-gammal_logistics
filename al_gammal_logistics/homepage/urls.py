from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("fleets/", views.fleets, name="fleets"),
    path("advantage/", views.advantage, name="advantage"),
    path("career/", views.career, name="career"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("articles/<int:article_id>/", views.articles, name="articles"),
    path("services/<int:service_id>/", views.services, name="services"),
    path("fleet/<int:fleet_id>/", views.fleet, name="fleet"),
    path("project/<int:project_id>/", views.project, name="project"),
    path("order/", views.CreateOrder.as_view(), name="create_order"),
    path("order_success/", TemplateView.as_view(template_name="homepage/order_success.html"), name="order_success"),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)