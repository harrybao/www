from django.urls import path
from ht import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('adv/',views.adv,name='adv'),
    path('book/',views.book,name='book'),
    path('cate/',views.cate,name='cate'),
    path('catedit/',views.catedit,name='catedit'),
    path('column/',views.column,name='column'),
    path('info/',views.info,name='info'),
    path('list/',views.list,name='list'),
    path('page/',views.page,name='page'),
    path('tips/',views.tips,name='tips'),
    path('pas/',views.pas,name='pas'),
]
