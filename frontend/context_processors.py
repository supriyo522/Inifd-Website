from backend.models import WebsiteSettings


def website_settings(request):
    """
    This function is used to pass website settings to the templates.
    """
    w_setting = WebsiteSettings.objects.get(id=1)
    return {
        'website_setting': w_setting
    }
