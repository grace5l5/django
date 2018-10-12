from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index),
    path('about-me', views.about_me),
    path('contact-me', views.contact_me),
    path('blogs', views.blogs),
    path('projects', views.projects),
    path('github-api-example', views.github_api_example),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


