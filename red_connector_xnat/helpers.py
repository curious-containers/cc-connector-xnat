import jsonschema

from requests.auth import HTTPBasicAuth


class ValidationError(Exception):
    pass


def auth_method_obj(access):
    if not access.get('auth'):
        return None

    auth = access['auth']

    return HTTPBasicAuth(
        auth['username'],
        auth['password']
    )


def validate(instance, schema):
    try:
        jsonschema.validate(instance, schema)
    except jsonschema.ValidationError as e:
        if hasattr(e, 'context') and e.context is not None:
            raise ValidationError(str(e.context))
        else:
            raise ValidationError(str(e))
