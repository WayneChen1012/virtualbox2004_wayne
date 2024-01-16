#include <iostream>
#include <string>

int main() {
    std::string city;
    std::cout << "請輸入一個城市名稱: ";
    std::getline(std::cin, city);
    std::cout << "歡迎來到 " << city << "！" << std::endl;
    return 0;
}