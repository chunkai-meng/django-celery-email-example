from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.conf import settings
from .tasks import mass_send, email_on_success


@csrf_exempt
@require_http_methods(["GET", "POST"])
def celery_email(request):

    if request.POST.get('token') == settings.CELERY_API_KEY:
        msg_id = request.POST.get('msg_id')
        email_from = request.POST['from']
        email_to = request.POST['to']
        subject = request.POST['subject']
        text_content = request.POST['text_content']
        html_content = request.POST['html_content']

        # add.apply_async((7,30), link=on_success.s())
        # result = mass_send.delay(1, email_from, email_to, subject,
        #                          text_content, html_content)
        result = mass_send.apply_async(
            (msg_id, email_from, email_to, subject, text_content, html_content),
            link=email_on_success.s())
        return HttpResponse(result)
    else:
        return HttpResponse('0')
