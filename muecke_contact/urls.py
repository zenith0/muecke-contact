# django imports
from django.conf.urls.defaults import *

urlpatterns = patterns('muecke_contact.views',
    url(r'^contact$', "contact_form", name='muecke_contact_form'),
    url(r'^contact-form-sent/$', "contact_form_sent", name='muecke_contact_form_sent'),
)
