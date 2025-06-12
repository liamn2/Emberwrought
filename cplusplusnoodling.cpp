#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}

// Collatz Algorithm
#include <iostream>

int collatz(int n) {
    int steps = 0;
    while (n != 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        steps++;
    }
    return steps;
}

int main() {
    int start_number = 6;
    int steps = collatz(start_number);
    std::cout << "The Collatz sequence for " << start_number << " takes " << steps << " steps to reach 1." << std::endl;
    return 0;
}
