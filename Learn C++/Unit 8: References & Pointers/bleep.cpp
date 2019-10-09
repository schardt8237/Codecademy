#include <iostream>
#include <string>
#include "functions.hpp"

int main() {
  std::string word = "broccoli";
  std::string text = "I never eat broccoli. There are three interesting things about broccoli. Number one, nobody knows how to spell it. Number two, no matter how long you boil it, it's always cold by the time it reaches your plate. Number three, it's green. #broccoli";
  
  bleep(word, text);
  
  std::cout << text;
}
