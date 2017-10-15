import socket
import time
import logging
import traceback
from django.utils.deprecation import MiddlewareMixin

__author__ = ["Arun Reghunathan"]

logger = logging.getLogger('requests')


class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        request.user = request.META.get('HTTP_USER_ID', 'Anonymous')
        request.app_version = request.META.get('HTTP_APP_VERSION', None)
        log_data= {
            "user": request.user,
            "remote_address": request.META['REMOTE_ADDR'],
            "server_hostname": socket.gethostname(),
            "request_method": request.method,
            "request_path": request.get_full_path(),
            "app_version": request.app_version,
        }
        if log_data["request_path"] in ['/project/reset/', '/project/corpsignin/'] and log_data['request_method'] == 'POST':
            log_data["request_body"] = "## Sensitive Info ##"
        else:
            log_data["request_body"] = request.body
        logger.info(log_data)

    def process_response(self, request, response):
        """
        The middleware processes the response before it is returned.

        The function serves the following purpose - logging error responses
        and exceptions when they occur and store them in the log.
        The response status_code is checked to see if the returned response
        has a status code of "200 - OK" or not.

        If the response is not "200", it is assumed that an exception has occurred
        and the exception is logged for analysis.

        The logger gives a detailed log of the system which include the params
        :user: the user who made the request
        :remote_address: The remote address from where the request was made
        :server_hostname: The hostname of the server where the request was made
        :request_method: The request method used
        :request_path: The API endpoint to which the request was made
        :request_body: The body of the HTTP request made
        :response_status: The custom error response status
        :run_time: The time taken to deliver the response`
        """
        # if not request.user or str(request.user) in ['Anonymous', 'AnonymousUser']:
        #     request.user = request.META.get('HTTP_USER_ID', 'Anonymous')

        # logger.info('Response sent for user {2} & endpoint {0}: {1} with status {3} '.format(request.method,
        #                                     request.get_full_path(),request.user, response.status_code))
        try:
            data = response.data
        except AttributeError:
            # response.data might not be present in case of html responses
            # data = response._container
            data = None
        logger.debug('Response data for {0}: {1}'.format(request.get_full_path(), data))
        DONOT_PRINT_RESPONSE = True  # False to write full response

        if DONOT_PRINT_RESPONSE:
            logger.info('Response data for {0}'.format(request.get_full_path()))
        # if is_client_error(response.status_code) or is_server_error(response.status_code):
        else:
            request_info = {
                "user": request.user,
                "remote_address": request.META['REMOTE_ADDR'],
                "server_hostname": socket.gethostname(),
                "request_method": request.method,
                "request_path": request.get_full_path(),
                "response": data,
                "response_status": response.status_code,
                "run_time": time.time() - request.start_time,
            }
            logger.info(request_info)
        return response


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        """
        The middleware processes the response before it is returned.

        The function serves the following purpose - logging error responses
        and exceptions when they occur and store them in the log.
        The response status_code is checked to see if the returned response
        has a status code of "200 - OK" or not.

        If the response is not "200", it is assumed that an exception has occurred
        and the exception is logged for analysis.

        The logger gives a detailed log of the system which include the params
        :user: the user who made the request
        :remote_address: The remote address from where the request was made
        :server_hostname: The hostname of the server where the request was made
        :request_method: The request method used
        :request_path: The API endpoint to which the request was made
        :request_body: The body of the HTTP request made
        :response_status: The custom error response status
        :run_time: The time taken to deliver the response`
        """
        user = request.user
        log_data = {
            "user": user,
            "remote_address": request.META['REMOTE_ADDR'],
            "server_hostname": socket.gethostname(),
            "request_method": request.method,
            "request_path": request.get_full_path(),
            "run_time": time.time() - request.start_time,
            "traceback": traceback.format_exc()
        }
        logger.error(log_data)
