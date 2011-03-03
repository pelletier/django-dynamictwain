from django.db import models


class TempFormData(models.Model):
    """

    """
    json_get = models.TextField()
    json_post = models.TextField()
    orig_url = models.TextField()
    scan = models.FileField(blank=False, upload_to='dynamictwain_temp')
