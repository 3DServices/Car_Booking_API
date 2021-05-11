from django.test import TestCase
from api.models import User
import uuid
# Create your tests here.


class TestUserModal(TestCase):
    def test_if_user_can_be_created(self):
        generatedId = '123e4567-e89b-12d3-a456-426614174000'
        user = User.objects.create(Id=generatedId)
        self.assertEqual(str(user.Id), str(generatedId))

    def test_existence_of_user_created(self):
        user = User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

        check_existence = User.objects.filter(first_name='timo').exists()
        self.assertEqual(check_existence, True)


# guidance with the crud operation
