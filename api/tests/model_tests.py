from django.test import TestCase
import api.models as api_models
import uuid
# Create your tests here.


class TestVehicleModal(TestCase):
    def setUp(self):
        vehicle = api_models.Vehicle.objects.create(
            type_of_vehicle='range-rover', carrying_capacity=5)

    def test_existence_of_vehicle_created(self):

        check_existence = api_models.Vehicle.objects.filter(
            type_of_vehicle='range-rover').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_vehicle_record(self):

        vehicle_store = api_models.Vehicle.objects.get(
            type_of_vehicle='range-rover')
        vehicle_store.type_of_vehicle = 'bmw'
        vehicle_store.save()
        check_existence = api_models.Vehicle.objects.filter(
            type_of_vehicle='bmw').exists()
        self.assertTrue(check_existence)

    def test_delete_of_vehicle_record(self):

        vehicle_store = api_models.Vehicle.objects.get(
            type_of_vehicle='range-rover')
        vehicle_store.delete()
        check_existence = api_models.Vehicle.objects.filter(
            type_of_vehicle='range-rover').exists()
        self.assertFalse(check_existence)


class TestOrganisationModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra', id=1)

    def test_existence_of_organisation_created(self):

        check_existence = api_models.Organisation.objects.filter(
            name='Unra').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_organisation_record(self):

        organisation_store = api_models.Organisation.objects.get(
            name='Unra')
        organisation_store.name = 'kakira'
        organisation_store.save()
        check_existence = api_models.Organisation.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_organisation_record(self):

        organisation_store = api_models.Organisation.objects.get(
            name='Unra')
        organisation_store.delete()
        check_existence = api_models.Organisation.objects.filter(
            name='Unra').exists()
        self.assertFalse(check_existence)


class TestProjectModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra')

        project = api_models.Project.objects.create(
            name='projectx', organisation=organisation)

    def test_existence_of_project_created(self):

        check_existence = api_models.Project.objects.filter(
            name='projectx').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_project_record(self):

        project_store = api_models.Project.objects.get(
            name='projectx')
        project_store.name = 'kakira'
        project_store.save()
        check_existence = api_models.Project.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_project_record(self):

        project_store = api_models.Project.objects.get(
            name='projectx')
        project_store.delete()
        check_existence = api_models.Project.objects.filter(
            name='projectx').exists()
        self.assertFalse(check_existence)
