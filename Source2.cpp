#include <iostream>
using namespace std;
#include <cmath>
int main()
{
    int h, m, s;
    int p, q, r;
    std::cout << "введите текущее время: ";
    std::cin >> h >> m >> s;
    std::cout << "сколько времени назад: ";
    std::cin >> p >> q >> r;
    long long currentseconds = h * 3600 + m * 60 + s;
    long long pastseconds = p * 3600 + q * 60 + r;
    long long totalsecondsinday = 24 * 3600;
    long long diffseconds = currentseconds - pastseconds
    int res_h = diffseconds / 3600;
    int res_m = (diffseconds % 3600) / 60;
    int res_s = diffseconds % 60;
    std::cout << "часы показывали: " << res_h << " ч. " << res_m << " мин. " << res_s << " сек." << std::endl;
    return 0;
}