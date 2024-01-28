Poker Probability Simulator
Overview
This Python project is a poker probability simulator that utilizes classes and methods to model a deck of cards, poker hands, and their respective probabilities. The code includes implementations of the Card, Deck, and PokerHand classes.

Classes

Card
Represents a playing card with attributes rank and suit.
Includes methods for retrieving and setting the rank and suit.
Defines comparison methods for card ranking.
Implements a user-friendly string representation.

Deck
Represents a standard deck of 52 playing cards.
Provides methods for dealing, shuffling, and cutting the deck.
Ensures proper initialization with a full deck during instantiation.

PokerHand
Models a poker hand, which is a collection of five cards.
Includes methods for adding cards to the hand, determining the type of poker hand, and displaying the hand.

Simulation
The project includes a simulation where poker hands are dealt and their probabilities are calculated over a large number of iterations (200,000). The results are categorized into different hand types such as high card, one pair, two pair, three of a kind, straight, flush, full house, four of a kind, and straight flush.

Usage
Clone the repository.
Run the poker_simulation.py file to simulate poker hand probabilities.
bash
Copy code
python poker_simulation.py
Results
The simulation outputs the number of occurrences for each hand type and calculates the corresponding probabilities. The results provide insights into the likelihood of different poker hands occurring in a random deck.

Feel free to explore and modify the code for educational purposes or to enhance your understanding of Python programming and poker probabilities.
