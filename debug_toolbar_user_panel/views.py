from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.conf import settings
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout as django_logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import UserForm
from .decorators import debug_required

@csrf_exempt
@require_POST
@debug_required
def login_form(request):
    form = UserForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    return login(request, **form.get_lookup())

@csrf_exempt
@require_POST
@debug_required
def login(request, **kwargs):
    user = get_object_or_404(get_user_model(), **kwargs)

    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    auth.login(request, user)

    return HttpResponseRedirect(request.POST.get('next', '/'))

@csrf_exempt
@require_POST
@debug_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect(request.POST.get('next', '/'))
