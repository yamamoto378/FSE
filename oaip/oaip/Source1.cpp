#include <iostream>

int main() {
    char letter;
    std::cout << "Введите одну из букв (P K T B L R): ";
    std::cin >> letter;
    switch (letter) {
    case 'P':
        std::cout << "Paris" << std::endl;
        break;
    case 'K':
        std::cout << "Copenhagen" << std::endl;
        break;
    case 'T':
        std::cout << "Tallinn" << std::endl;
        break;
    case 'B':
        std::cout << "Berlin" << std::endl;
        break;
    case 'L':
        std::cout << "London" << std::endl;
        break;
    case 'R':
        std::cout << "Rome" << std::endl;
        break;
    default:
        std::cout << "Ошибка:введенн неверный символ" << std::endl;
    }
    return 0;
}