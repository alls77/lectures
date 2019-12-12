from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View


class MyView(PermissionRequiredMixin, View):
    permission_required = 'polls.can_vote'
    # Or multiple of permissions:
    permission_required = ('polls.can_open', 'polls.can_edit')