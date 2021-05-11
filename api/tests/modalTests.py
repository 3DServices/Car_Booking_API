from django.test import TestCase
from api.models import User
import uuid
# Create your tests here.


class TestUserModal(TestCase):
    def test_uuid(self):
        generatedId = uuid.uuid4()
        user = User.objects.create(Id=generatedId)
        self.assertEqual(str(user.Id), str(generatedId))

    def test_existence_of_user_created(self):
        user = User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

        check_existence = User.objects.filter(first_name='timo').exists()
        self.assertEqual(check_existence, True)
