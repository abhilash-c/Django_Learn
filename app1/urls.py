from django.urls import path
from . import views
urlpatterns = [
    path('', views.page1, name="home page"),
    path('2/',views.page2, name= "home 2"),
    path('3/',views.page_html,name="html"),
    path('4/',views.page_table,name="table"),
    path("form/",views.forms),
    path("sql/",views.form2)
]

