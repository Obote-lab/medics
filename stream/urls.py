from django.urls import path
from .views import streamlit_view

urlpatterns = [
    path('streamlit/', streamlit_view, name='streamlit_view'),
    # ... other URLs in your app
]
