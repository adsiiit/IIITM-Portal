from django.conf.urls import patterns, url, include
from iiitm import views



urlpatterns = patterns('',
        url(r'^about/$', views.about, name='about'),
        url(r'^complaint/', views.add_complaint, name='complaint'),
        url(r'^complaint_status/', views.complaint_status, name='complaint_status'),
        url(r'^library_status/', views.library_status, name='library_status'),
        url(r'^issue_status/', views.issue_status, name='issue_status'),
        url(r'^accounts/', views.accounts, name='accounts'),
        url(r'^administration/', views.administration, name='administration'),
        url(r'^faculty_status/', views.faculty_status, name='faculty_status'),
        url(r'^academics/', views.academics, name='academics'),
        url(r'^activities/$', views.activities, name='activities'),
        )