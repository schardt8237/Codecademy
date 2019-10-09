#include <iostream>

int main() {
  // age of dog
  int dog_age = 8;
  
  int early_years, later_years ,human_years;
  
  // The first two years
  early_years = 21;
  later_years = (dog_age - 2) * 4;
  human_years = early_years + later_years;
  
  std::cout << "My name is Bailey! Ruff ruff, I am " << human_years << " years old in human years.";
}
