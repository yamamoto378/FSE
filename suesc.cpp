#include <iostream>
using namespace std;
#include <cmath> 
int main()
{
    double x1, y1, x2, y2, x3, y3;
    cout << "введите координаты первой вершины (x1, y1): ";
    cin >> x1 >> y1;

    cout << "введите координаты второй вершины (x2, y2): ";
    cin >> x2 >> y2;

    cout << "введите координаты третьей вершины (x3, y3): ";
    cin >> x3 >> y3;
    double side1 = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    double side2 = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double side3 = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));
    cout << "\nдлины сторон треугольника:\n";
    cout << "сторона1: " << side1 << endl;
    cout << "сторона2: " << side2 << endl;
    cout << "сторона3: " << side3 << endl;

    return 0;
}