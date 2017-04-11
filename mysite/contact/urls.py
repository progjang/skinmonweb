from django.conf.urls import url

#import views as contact_views
from views import ContactFormView
urlpatterns = [
    #url(r'^$', contact_views.contact, name='contact'),
    url(r'^$', ContactFormView.as_view(), name='contact'),

]