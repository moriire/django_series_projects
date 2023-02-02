from django.shortcuts import render
from contacts.models import Contact
# Create your views here.
def index(request):
	greetings = "I created this app in less than 20mins"
	contacts = Contact.objects.all()
	return render(request, "index.html", context={"greetings": greetings, "contacts": contacts})