from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import logging


logger = logging.getLogger(__name__)


# Create your views here.
def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        logger.info('Received!!!!')
        if not form.is_valid():
            return render(request, 'converter/index.html', {'form': form})

        content = handle_uploaded_file(request.FILES['upload_file'])
        # logger.info('content %s' % content)
        response = HttpResponse(content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'inline; filename=' + str(request.FILES['upload_file'])
        return response
    else:
        form = UploadFileForm()
    return render(request, 'converter/index.html', {'form': form})


def handle_uploaded_file(f):
    # logger.info('Success!!!')
    content = f.read()
    return content
