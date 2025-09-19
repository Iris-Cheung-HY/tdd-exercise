from main import blackjack_score
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  # Arrange
  hand = ["King", 5]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 15

@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  # Arrange
  hand = [9, "Ace"]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 20


@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  # Arrange
  hand = [9, 3, "Ace"]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 13  


@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  # Arrange
  hand = [9, "Joker"]

  # Act
  score = blackjack_score(hand)

  #Assert
  assert score is None
    


@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  # Arrange
  hand = [4,5,6,7,8,9]

  #Act
  score = blackjack_score(hand)
  #Assert
  assert score is None 


@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [9, 8, 7]

  score = blackjack_score(hand)

  assert ("You Busted")

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ["Ace", "Ace", "King"]

  score = blackjack_score(hand)

  assert score == 12

#@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  hand = ["Ace", "Ace", "Ace", "Ace",]

  score = blackjack_score(hand)

  assert score == 14
