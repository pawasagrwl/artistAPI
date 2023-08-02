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


from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Artist

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        Artist.objects.create(user=instance)