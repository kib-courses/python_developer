import unittest
from lecture_13.matrix.matrixapp.actors import Neo, Morpheus, WhiteRabbit


class TestActors(unittest.TestCase):
    def setUp(self) -> None:
        self.neo = Neo()
        self.morpheus = Morpheus()
        self.white_rabbit = WhiteRabbit()

    def test_neo_morpheus(self):
        """
        Replica of Neo with Morpheus
        """
        self.assertIsNotNone(self.neo.interact(self.morpheus))

    def test_morpheus_wr(self):
        """
        Replica of Morpheus with WhiteRabbit
        """
        self.assertRegex(self.morpheus.interact(self.white_rabbit), 'strangers')

    def test_wr_neo(self):
        """
        Replica of WhiteRabbit with Neo
        """
        self.assertIsNotNone(self.white_rabbit.interact(self.neo))

    def tearDown(self) -> None:
        del self.neo
        del self.morpheus
        del self.white_rabbit
