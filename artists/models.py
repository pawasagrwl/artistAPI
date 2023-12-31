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

from django.db import models
from django.contrib.auth.models import User

class Work (models.Model):
    WORK_TYPE_CHOICES = [
        ("YT", "Youtube"),
        ("IG", "Instagram"),
        ("OT", "Other")
    ]
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPE_CHOICES, default="YT")
## artist should only be created when a user is created
class Artist (models.Model):
    user = models.OneToOneField (User, on_delete = models.CASCADE)
    name = models.CharField(max_length=25)
    work = models.ManyToManyField(Work)