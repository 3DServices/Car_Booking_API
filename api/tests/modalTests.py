from django.test import TestCase
from api.models import User
import uuid
# Create your tests here.


class TestUserModal(TestCase):
    def test_uuid(self):
        generatedId = uuid.uuid4()
        user = User.objects.create(Id=generatedId)
        self.assertEqual(str(user.Id), str(generatedId))

    def test_uuid(self):
        generatedId = uuid.uuid4()
        user = User.objects.create(Id=generatedId)
        self.assertEqual(str(user.Id), str(generatedId))
