from django.test import TestCase

from vanilla.models import News

class TestMigrations(TestCase):
    def test_if_database_will_migrate(self):
        News.objects.all()
