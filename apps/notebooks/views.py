# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       authentication_classes,
                                       permission_classes,
                                       throttle_classes,)
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework_expiring_authtoken.authentication import (ExpiringTokenAuthentication,)
from accounts.permissions import HasVerifiedEmail

# Create your views here.
@throttle_classes([UserRateThrottle])
@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated, HasVerifiedEmail))
@authentication_classes((ExpiringTokenAuthentication,))
def notebook_list(request, challenge_host_team_pk):
    pass
