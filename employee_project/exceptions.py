from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {}
        custom_response['errors'] = response.data
        return Response(custom_response, status=response.status_code)

    # If response is None, means server error (500 etc.)
    return Response(
        {'errors': 'Something went wrong. Please try again later.'},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
