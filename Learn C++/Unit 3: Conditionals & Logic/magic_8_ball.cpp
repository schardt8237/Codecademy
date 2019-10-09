#include <iostream>
#include <cstdlib>

int main() {

  // Your future is here
	std::cout << "MAGIC 8-BALL:" << std::endl;
  
  srand(time(NULL));
  
  int answer = std::rand() % 10;
  
  if(answer == 0) {
    std::cout << "It is certain.";
  }
  else if(answer == 1) {
    std::cout << "It is quite possible.";
  }
  else if(answer == 2) {
    std::cout << "For sure.";
  }
  else if(answer == 3) {
    std::cout << "Yes, absolutely.";
  }
  else if(answer == 4) {
    std::cout << "I'd put money on it.";
  }
  else if(answer == 5) {
    std::cout << "It would seem so.";
  }
  else if(answer == 6) {
    std::cout << "Ask some other time.";
  }
  else if(answer == 7) {
    std::cout << "I'd wouldn't put money on it.";
  }
  else if(answer == 8) {
    std::cout << "I'm not feeling it.";
  }
  else {
    std::cout << "Very doubtful.";
  }
}
