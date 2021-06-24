from django.test import TestCase

from core.celery import add
from apps.simc.battle.battle_flow import BattleFlow


# Create your tests here.


class ModelsTest(TestCase):
    def test_001(self):
        task = add.delay(1, 2)

# Create your tests here.
