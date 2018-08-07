from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import logging
from .converter import Converter


logger = logging.getLogger(__name__)


# Create your views here.
def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        logger.info('Received!!!!')
        if not form.is_valid():
            return render(request, 'converter/index.html', {'form': form})

        file = request.FILES['upload_file']
        convert_type = request.POST.get('convert_type')
        charset_type = request.POST.get('charset_type')
        sync_ms = request.POST.get('sync_ms')

        content = Converter.handle_uploaded_file(file, convert_type, charset_type, sync_ms)
        response = HttpResponse(content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'inline; filename=' + str(request.FILES['upload_file'])
        return response
    else:
        form = UploadFileForm()
    return render(request, 'converter/index.html', {'form': form})
