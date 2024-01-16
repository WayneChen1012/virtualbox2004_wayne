#include <iostream>
#include <string>

int main() {
    std::string city;
    std::cout << "type some words: ";
    std::getline(std::cin, city);
    std::cout << "welcome ~ " << city << "！" << std::endl;
    return 0;
}
