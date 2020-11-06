import json


def make_get_request(app_instance, url, params=None):
    response = app_instance.get(url, data=params)
    status_code = response.status_code
    json_response = json.loads(response.data)
    return status_code, json_response


def make_post_request(app_instance, url, data={}, headers={}):

    response = app_instance.post(
        url, json=data, content_type="application/json", headers=headers
    )
    status_code = response.status_code
    json_response = json.loads(response.data)
    return status_code, json_response


