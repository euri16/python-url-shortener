import re
from flask import make_response
import safejson

CONTENT_TYPE_JSON = "application/json"


def prepare_response(error, msg, code, content_type=CONTENT_TYPE_JSON,
                     response=None):
    """ Get the response json including response data """
    response = make_response(api_response(error, msg, response), code)
    response.headers["Content-Type"] = content_type
    response.mimetype=content_type
    return response


def api_response(error, response_msg, response_code, response=None,
                 response_dict=None):
    """
    Method to create a response
    :param error:bool
    :param response_code:int
    :param response_msg:str
    :param response:dict=None
    :param response_dict:dict=None
    :return:str
    """
    obj = {"error": error,
           "response_msg": response_msg,
           "response": response}

    if response_dict is not None:  # pragma: no cover
        response_data = obj.copy()
        response_data.update(response_dict)
        return safejson.dumps(response_data, sort_keys=False)

    return json_response(make_response(safejson.dumps(obj, sort_keys=False),
                                       response_code))


def json_response(response):
    response.mimetype = CONTENT_TYPE_JSON
    return response
