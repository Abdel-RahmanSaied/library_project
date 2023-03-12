from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Author
from .serializers import *
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection
from rest_framework.permissions import AllowAny


# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'id']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'id']

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'id']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'id']

class PurchasesViewSet(viewsets.ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']

class RentsViewSet(viewsets.ModelViewSet):
    queryset = Rents.objects.all()
    serializer_class = RentsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']


class AutherViewSet_callProc(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'id']

    def create(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('create_author', [request.data['full_name'],
                                              request.data['email'],
                                              request.data['address'],
                                              request.data['phone'],
                                              request.data['birth_date'],
                                              ])


            return Response(result_set, status=status.HTTP_201_CREATED)
        finally:
            cursor.close()

    def list(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('index_authors', )
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()

    def retrieve(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('get_author_by_id', [pk])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()

    def update(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('update_author', [pk,
                                              request.data['full_name'],
                                              request.data['email'],
                                              request.data['address'],
                                              request.data['phone'],
                                              request.data['birth_date'],
                                              ])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()

    def destroy(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('remove_author_by_id', [pk])
            # result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()


class BookViewSet_callProc(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Author.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'id']

    def create(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('create_book', [request.data['title'],
                                              request.data['description'],
                                              request.data['price'],
                                              request.data['rent_fee'],
                                              request.data['release_year'],
                                              request.data['author'],
                                              request.data['quantity'],
                                              request.data['category'],
                                                         ])
            return Response(result_set, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def list(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('index_books', )
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()

    def retrieve(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('get_book_by_id', [pk])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()

    def update(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('update_book', [request.data['id'],
                                              request.data['title'],
                                              request.data['author_id'],
                                              request.data['genre'],
                                              request.data['price'],
                                              request.data['publish_date'],
                                              request.data['description'],
                                              request.data['image'],
                                              request.data['quantity'],
                                              request.data['rating'],
                                              ])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()

    def destroy(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('remove_book_by_id', [pk])
            # result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        finally:
            cursor.close()


class CustomerViewSet_callProc(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Author.objects.all()
    serializer_class = CustomerSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'id']

    def create(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('create_customer', [request.data['full_name'],
                                              request.data['email'],
                                              request.data['address'],
                                              request.data['phone'],
                                              ])
            return Response(result_set, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def list(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('index_customers', )
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def retrieve(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('get_customer_by_id', [pk])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def update(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('update_customer', [pk,
                                              request.data['full_name'],
                                              request.data['email'],
                                              request.data['address'],
                                              request.data['phone'],
                                              request.data['birth_date'],
                                              ])
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def destroy(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('remove_customer_by_id', [pk])
            # result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

class EmployeeViewSet_callProc(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Author.objects.all()
    serializer_class = EmployeeSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'id']

    def create(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('create_employee', [request.data['full_name'],
                                              request.data['email'],
                                              request.data['address'],
                                              request.data['phone'],
                                              request.data['position'],
                                              request.data['salary'],
                                              request.data['birth_date'],
                                              ])
            return Response(result_set, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def list(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('index_employees', )
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def retrieve(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('get_employee_by_id', [pk])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def update(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('update_employee', [pk,
                                              request.data['full_name'],
                                              request.data['email'],
                                              request.data['address'],
                                              request.data['phone'],
                                              request.data['position'],
                                              request.data['salary'],
                                              request.data['birth_date'],
                                              ])
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def destroy(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('remove_employee_by_id', [pk])
            # result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

class PurchasesViewSet_callProc(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Author.objects.all()
    serializer_class = PurchasesSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'id']

    def create(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('create_purchase', [
                                              request.data['book'],
                                              request.data['customer'],
                                              request.data['purchase_date'],
                                              request.data['employee'],

                                              ])
            return Response(result_set, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def list(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('index_purchases', )
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def retrieve(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('get_purchase_by_id', [pk])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def update(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('update_purchase', [pk,
                                                request.data['book'],
                                                 request.data['customer'],
                                                 request.data['purchase_date'],
                                                 request.data['employee'],
                                                 ])
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def destroy(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('remove_purchase_by_id', [pk])
            # result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

class RentsViewSet_callProc(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    # queryset = Author.objects.all()
    serializer_class = RentsSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'id']

    def create(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('create_rent', [
                                              request.data['book'],
                                              request.data['customer'],
                                              request.data['employee'],
                                              request.data['rent_date'],
                                              request.data['return_date'],

                                              ])
            return Response(result_set, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def list(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        cursor = connection.cursor()
        try:
            cursor.callproc('index_rents', )
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def retrieve(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('get_rent_by_id', [pk])
            result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def update(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            cursor.callproc('update_rent', [pk,
                                                request.data['book'],
                                                 request.data['customer'],
                                                 request.data['rent_date'],
                                                 request.data['return_date'],
                                                 request.data['employee'],
                                                 ])
            result_set = cursor.fetchall()
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()

    def destroy(self, request, *args, **kwargs):
        # use cursor to call stored procedure
        pk = kwargs['pk']
        cursor = connection.cursor()
        try:
            result_set = cursor.callproc('remove_rent_by_id', [pk])
            # result_set = cursor.fetchall()
            print(result_set)
            return Response(result_set, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            cursor.close()


# class Author(APIView):
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         cursor = connection.cursor()
#         # WRITE CALL TO STORED PROCEDURE HERE
#         try:
#             cursor.callproc('get_author_by_id', [1])
#             result_set = cursor.fetchall()
#             print(result_set)
#             return Response(result_set, status=status.HTTP_200_OK)
#         finally:
#             cursor.close()
#
#         # return Response(result_set)