from datetime import datetime

from django.http import HttpResponse
from django.utils import formats
from django.utils.translation import gettext as _


def first(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)


def date_view(request):
    d = datetime.now().day
    m = _(datetime.now().strftime('%B'))

    output = _('Today is %(month)s %(day)s.') % {'month': m, 'day': d}
    return HttpResponse(output)
