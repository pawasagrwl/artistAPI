# This file is part of ArtistAPI.
#
# ArtistAPI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ArtistAPI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ArtistAPI.  If not, see <https://www.gnu.org/licenses/>.


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ArtistViewSet, WorkViewSet, RegisterView
from rest_framework.authtoken.views import obtain_auth_token 

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('artists', ArtistViewSet, basename='artists')
router.register('works', WorkViewSet, basename='works')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', obtain_auth_token, name='login'),  # get existing auth token
]
