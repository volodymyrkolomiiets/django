from django.conf.urls import url 
from django.contrib.auth.decorators import login_required, permission_required 

urlpatterns = [ 
    url(r'^users_only/', login_required(myview)), 

    url(r'^category/', permission_required('myapp.change_category', login_url='login')(myview)), 
] 