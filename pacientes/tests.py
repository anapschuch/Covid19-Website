from django.urls import reverse
from django.test import TestCase
from .views import home, patient_description
from django.urls import resolve
from .models import Paciente
from datetime import date


class HomeTests(TestCase):
    def setUp(self):
        self.patient = Paciente.objects.create(nome='João da Silva', idade=70, data_inicio_sintomas=date.today(),
                                               temperatura_maxima=38)
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_patients_page(self):
        patients_description_url = reverse('patient_description', kwargs={'pk': self.patient.pk})
        self.assertContains(self.response, 'href="{0}"'.format(patients_description_url))


class PatientsDescriptionTests(TestCase):
    def setUp(self):
        Paciente.objects.create(nome='João da Silva', idade=70, data_inicio_sintomas=date.today(),
                                temperatura_maxima=38)

    def test_patient_description_view_success_status_code(self):
        url = reverse('patient_description', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_patient_description_view_not_found_status_code(self):
        url = reverse('patient_description', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_patient_url_resolves_pacient_topics_view(self):
        view = resolve('/pacientes/1/')
        self.assertEquals(view.func, patient_description)

    def test_patient_view_contains_link_back_to_homepage(self):
        patient_url = reverse('patient_description', kwargs={'pk': 1})
        response = self.client.get(patient_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
