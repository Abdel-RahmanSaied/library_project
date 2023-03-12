from django.urls import path, include
from rest_framework import routers
from .views import *

routers = routers.DefaultRouter()
routers.register('author', AuthorViewSet)
routers.register('book', BookViewSet)
routers.register('customer', CustomerViewSet)
routers.register('employee', EmployeeViewSet)
routers.register('purchases', PurchasesViewSet)
routers.register('rents', RentsViewSet)

# urls for views with callproc methods
routers.register('authorCallProc', AutherViewSet_callProc, basename='authorCallProc')
routers.register('BookCallProc', BookViewSet_callProc, basename='BookCallProc')
routers.register('CustomerCallProc', CustomerViewSet_callProc, basename='CustomerCallProc')
routers.register('EmployeeCallProc', EmployeeViewSet_callProc, basename='EmployeeCallProc')
routers.register('PurchasesCallProc', PurchasesViewSet_callProc, basename='PurchasesCallProc')
routers.register('RentsCallProc', RentsViewSet_callProc, basename='RentsCallProc')

urlpatterns = [
    # path('authorView/', Author.as_view(), name='authorView'),
]

urlpatterns += routers.urls