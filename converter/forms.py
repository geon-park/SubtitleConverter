from django import forms


class UploadFileForm(forms.Form):
    upload_file = forms.FileField()
    convert_type = forms.CharField(max_length=8)
    charset_type = forms.CharField(max_length=8)
