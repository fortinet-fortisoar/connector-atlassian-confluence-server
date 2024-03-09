""" Copyright start
  Copyright (C) 2008 - 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import json
import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('atlassian-confluence-server')


class Confluence(object):
    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = ('https://{0}'.format(self.server_url))
        self.username = config.get('username')
        self.password = config.get('password')
        self.verify_ssl = config.get('verify_ssl')

    def make_rest_call(self, endpoint, params=None, payload=None, method='GET'):
        service_endpoint = '{0}/rest/api/{1}'.format(self.server_url, endpoint)
        logger.debug('API Request Endpoint: {0}'.format(service_endpoint))
        logger.debug('API Request Payload: {0}'.format(payload))
        logger.debug('API Request Params: {0}'.format(params))
        credentials = (self.username, self.password)
        try:
            response = requests.request(method, service_endpoint, auth=credentials, params=params, data=payload,
                                        verify=self.verify_ssl,
                                        headers={"Content-Type": "application/json", "Accept": "application/json"},
                                        timeout=600)
            logger.debug('API Status Code: {0}'.format(response.status_code))
            if response.ok:
                content_type = response.headers.get('Content-Type')
                if response.text != "" and 'application/json' in content_type:
                    return response.json()
                else:
                    return response.content
            else:
                if response.text != "":
                    err_resp = response.json()
                    raise ConnectorError(str(err_resp))
                else:
                    error_msg = '{0}: {1}'.format(response.status_code, response.reason)
                    raise ConnectorError(error_msg)
        except requests.exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except requests.exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except requests.exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except requests.exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))


def build_params(params):
    return {k: v for k, v in params.items() if v is not None and v != ''}


def get_spaces_list(config, params):
    con = Confluence(config)
    params = build_params(params)
    if params.get('type'):
        params['type'] = params.get('type').lower()
    if params.get('status'):
        params['status'] = params.get('status').lower()
    endpoint = 'space'
    resp = con.make_rest_call(endpoint, params=params)
    return resp


def create_space(config, params):
    con = Confluence(config)
    payload = {
        "key": params.get('key'),
        "name": params.get('name'),
        "description": {
            "plain": {
                "value": params.get('description'),
                "representation": "plain"
            }
        },
        "metadata": {}
    }
    endpoint = 'space'
    resp = con.make_rest_call(endpoint, payload=json.dumps(payload), method='POST')
    return resp


def get_content_list(config, params):
    con = Confluence(config)
    params = build_params(params)
    endpoint = 'content'
    resp = con.make_rest_call(endpoint, params=params)
    return resp


def create_content(config, params):
    con = Confluence(config)
    payload = {
        "type": params.get('type'),
        "title": params.get('title'),
        "space": {
            "key": params.get('space')
        },
        "body": {
            "storage": {
                "value": params.get('body'),
                "representation": "storage"
            }
        }
    }
    endpoint = 'content'
    resp = con.make_rest_call(endpoint, payload=json.dumps(payload), method='POST')
    return resp


def update_content(config, params):
    con = Confluence(config)
    payload = {
        "version": {
            "number": params.get('version')
        },
        "type": params.get('type')
    }
    if params.get('space'):
        payload['space'] = {"key": params.get('space')}
    if params.get('title'):
        payload['title'] = params.get('title')
    if params.get('body'):
        payload['body'] = {
            "storage": {
                "value": params.get('body'),
                "representation": "storage"
            }
        }
    endpoint = 'content/' + str(params.get('contentId'))
    resp = con.make_rest_call(endpoint, payload=json.dumps(payload), method='PUT')
    return resp


def delete_content(config, params):
    con = Confluence(config)
    endpoint = 'content/' + str(params.get('contentId'))
    resp = con.make_rest_call(endpoint, method='DELETE')
    return resp


def get_content_list_using_cql(config, params):
    con = Confluence(config)
    params = build_params(params)
    endpoint = 'content/search'
    resp = con.make_rest_call(endpoint, params=params)
    return resp


def _check_health(config):
    try:
        params = {}
        get_spaces_list(config, params)
        return True
    except Exception as e:
        raise ConnectorError('{0}'.format(e))


operations = {
    'get_spaces_list': get_spaces_list,
    'create_space': create_space,
    'get_content_list': get_content_list,
    'create_content': create_content,
    'update_content': update_content,
    'delete_content': delete_content,
    'get_content_list_using_cql': get_content_list_using_cql
}
