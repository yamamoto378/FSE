#include <iostream>

using namespace std;

int main() {

    double x, y;
    cout << "введите координаты точки x и y: ";
    cin >> x >> y;

    double r2 = x * x + y * y;

    if (x >= -2 && x <= 6 && y >= -6 && y <= 2
        && r2 >= 4
        && !(x > 0 && y < 0 && r2 > 16 && r2 < 36))
        cout << "точка принадлежит заштрихованной области" << endl;
    else
        cout << "точка не принадлежит заштрихованной области" << endl;

    return 0;
}