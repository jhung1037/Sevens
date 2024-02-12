import pytest


from Sevens import Card, Player

class TestPlayer:
    @pytest.fixture
    def player():
        return Player([Card(colour="S", num="A")])

    def test_play_card(player):
        player.play_card("SA")
        assert player.deck == []
