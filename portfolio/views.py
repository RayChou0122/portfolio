from django.shortcuts import render
from gallery.models import Gallery

def home(request):
	galleries = Gallery.objects
	return render(request,'home.html',{'galleries':galleries})