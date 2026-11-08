#include <iostream>
#include <cctype> 

int main() {
    char letter;
    std::cout << "Введите одну из букв (A, S, D, F, B, R): ";
    std::cin >> letter;

    letter = std::toupper(letter);

    switch (letter) {
    case 'A':
        std::cout << "Apple" << std::endl;
        break;
    case 'S':
        std::cout << "Sun" << std::endl;
        break;
    case 'D':
        std::cout << "Door" << std::endl;
        break;
    case 'F':
        std::cout << "Frog" << std::endl;
        break;
    case 'B':
        std::cout << "Banana" << std::endl;
        break;
    case 'R':
        std::cout << "River" << std::endl;
        break;
    default:
        std::cout << "Ошибка: введен неверный символ!" << std::endl;
        break;
    }

    return 0;
}
