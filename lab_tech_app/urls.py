from django.conf.urls import url

import lab_tech_app.views as views

urlpatterns = [
    url(r'^add$', views.LabView.as_view({'post':'addpatient'}),name='addpatient'),
    url(r'^list$', views.LabView.as_view({'get':'listall'}),name='listpatients'),
    url(r'^get$', views.LabView.as_view({'get':'getpatient'}),name='getpatient'),
    url(r'^delete$', views.LabView.as_view({'delete':'deletepatient'}),name='deletepatient'),
    url(r'^update$', views.LabView.as_view({'put':'updatepatient'}),name='updatepatient'),
]