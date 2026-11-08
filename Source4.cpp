#include <iostream>

using namespace std;

int main() {

    double x, y;
    cout << "введите координаты точки x и y: ";
    cin >> x >> y;
    double r2 = x * x + y * y;
    if ((x >= 0 && x * x + y * y <= 9) || (x < 0 && y >= -3 && y <= 3 && abs(y) >= -x))
        cout << "точка принадлежит заштрихованной области" << endl;
    else
        cout << "точка не принадлежит заштрихованной области" << endl;
}