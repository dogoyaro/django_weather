from django.conf import settings

def get_app_Id():
    """ get weather application Id """
    app_id = settings.APP_ID
    return app_id