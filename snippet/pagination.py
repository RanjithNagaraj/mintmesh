from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(pagination.CursorPagination):
    page_size = 2
    cursor_query_param = 'c'
    ordering = '-id'