from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
def streamlit_view(request):
    return render(request, 'streamlit_app.html')

