from rest_framework.response import Response
from rest_framework.status import is_success, HTTP_200_OK

__author__ = ["Arun Reghunathan"]


class CustomResponse(Response):
    def __init__(self, message=None, status=HTTP_200_OK, data={}, etype=None,
                 template_name=None, headers=None, app_version=None,
                 exception=False, content_type='application/json', **kwargs):

        response_data = dict()
        response_data['status_code'] = status
        if is_success(status):
            response_data['status'] = 'Success'
            response_data['data'] = data
            response_data.update(kwargs)

        else:
            response_data['status'] = 'Failed'
            error_data = dict(code=status, message=message)
            if exception:
                error_data['type'] = exception
            response_data['error'] = error_data

        super(CustomResponse, self).__init__(data=response_data, status=status, template_name=template_name,
                                             headers=headers, exception=exception, content_type=content_type)
