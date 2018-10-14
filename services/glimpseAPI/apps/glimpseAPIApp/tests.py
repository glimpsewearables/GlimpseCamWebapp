# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.test import TestCase
from .models import Media

# Create your tests here.

class JsonifyTestCase(TestCase):
	def setUp(self):
		Media.objects.create(
				id="123",
				user_id="456",
				device_id="789",
				event_id="123",
				media_type="image",
				raw_or_edited="raw",
				downloaded="no",
				ranking="0",
				created_at=datetime.time,
				updated_at=datetime.time,
			)

	def test_jsonify_media_data(self):
		media = Media.objects.get(id="123")
		context = jsonifyMediaData(media)
		self.assertEqual(context[media.link], {
                "id" : "123",
                "user_id" : "456",
                "device_id" : "789",
                "event_id" : "123",
                "media_type" : "image",
                "raw_or_edited" : "raw",
                "downloaded" : "no",
                "ranking" : "0",
                "created_at" : media.created_at,
                "updated_at" : media.updated_at
            })