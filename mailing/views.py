from django.views.generic import CreateView

from .models import ContactData
from .forms import ContactDataForm

class ContactDataView(CreateView):
    model = ContactData
    form_class = ContactDataForm
    success_url = '/'
