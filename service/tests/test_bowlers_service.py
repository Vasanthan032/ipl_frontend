from django.test import TestCase
from service.bowlers import BowlersService

class ServiceTest(TestCase):

  def test_get_top_10_bowlers(self):
    """Testing Top Wicket Tacker API"""
    bowler_service = BowlersService()
    result = bowler_service.get_top_10_bowlers('overall')
    print(result)
    self.assertTrue(result is not None)

  def test_bowlers_match_wise(self):
    """Testing Bowlers details match wise"""
    bowler_service = BowlersService()
    result = bowler_service.get_bowlers_match_wise('overall')
    print(result)
    self.assertTrue(result is not None)
