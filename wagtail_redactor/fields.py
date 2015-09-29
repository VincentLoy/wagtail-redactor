from django.forms.fields import CharField
from django.conf import settings
from redactor.widgets import RedactorEditor


class RedactorField(CharField):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('redactor_options', {})
        upload_to = kwargs.pop('upload_to', '')
        allow_file_upload = kwargs.pop('allow_file_upload', True)
        allow_image_upload = kwargs.pop('allow_image_upload', True)
        self.widget = RedactorEditor(
            redactor_options=options,
            upload_to=upload_to,
            allow_file_upload=allow_file_upload,
            allow_image_upload=allow_image_upload
        )
        super(RedactorField, self).__init__(*args, **kwargs)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^redactor\.fields\.RedactorField"])
