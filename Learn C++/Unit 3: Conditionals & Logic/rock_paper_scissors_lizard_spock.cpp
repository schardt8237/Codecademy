/*
Rock, Paper, Scissors, Lizard, Spock
A modified version of the classic kids game as seen in the TV show The Big Bang Theory.
*/

#include <iostream>
#include <stdlib.h>

enum Choices {
  Rock = 1,
  Paper,
  Scissors,
  Lizard,
  Spock
};

int main() {

  // Live long and prosper
  srand(time(NULL));
  
  int computer = rand() % 3 + 1;
  
  int user = 0;
  
  std::cout << "=================================\n";
  std::cout << "rock paper scissors lizard spock!\n";
  std::cout << "=================================\n";

  std::cout << "1) ✊\n";
  std::cout << "2) ✋\n";
  std::cout << "3) ✌️\n";
  std::cout << "4) lizard\n";
  std::cout << "5) spock\n";

  std::cout << "shoot! ";
  
  std::cin >> user;
  
  switch(user) {
    case Rock:
      std::cout << "you chose: ✊\n";
      break;
    case Paper:
      std::cout << "you chose: ✋\n";
      break;
    case Scissors:
      std::cout << "you chose: ✌️\n";
      break;
    case Lizard:
      std::cout << "you chose: lizard\n";
      break;
    case Spock:
      std::cout << "you chose: spock\n";
      break;
    default:
      std::cout << "invalid choice\n";
      break;
  }
  
  switch(computer) {
    case Rock:
      std::cout << "CPU chose: ✊\n";
      break;
    case Paper:
      std::cout << "CPU chose: ✋\n";
      break;
    case Scissors:
      std::cout << "CPU chose: ✌️\n";
      break;
    case Lizard:
      std::cout << "you chose: lizard\n";
      break;
    case Spock:
      std::cout << "you chose: spock\n";
      break;
  }
  
  if(user == computer) {
    std::cout << "Tie!\n";
  }
  else if (user == Rock) {
    if (computer == Scissors || computer == Lizard) {
      std::cout << "you win! yay!\n";
    }
    else {
      std::cout << "you lose! no!\n";
    }
  }
  else if (user == Paper) {
    if (computer == Rock || computer == Spock) {
      std::cout << "you win! yay!\n";
    }
    else {
      std::cout << "you lose! no!\n";
    }
  }
  else if (user == Scissors) {
    if (computer == Paper || computer == Lizard) {
      std::cout << "you win! yay!\n";
    }
    else {
      std::cout << "you lose! no!\n";
    }
  }
  else if (user == Lizard) {
    if (computer == Paper || computer == Spock) {
      std::cout << "you win! yay!\n";
    }
    else {
      std::cout << "you lose! no!\n";
    }
  }
  else if (user == Spock) {
    if (computer == Rock || computer == Scissors) {
      std::cout << "you win! yay!\n";
    }
    else {
      std::cout << "you lose! no!\n";
    }
  }
}
