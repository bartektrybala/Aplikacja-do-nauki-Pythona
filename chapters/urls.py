"""Defines URL patterns for chapters."""

from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all chapters and topics
    path('chapters/', views.chapters, name='chapters'),
    path('chapters/<int:chapter_id>/', views.topic, name='topic'),

    # Approach for the topic
    path('topic/<int:topic_id>', views.approach, name='approach')
]

