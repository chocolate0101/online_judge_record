/*
Bee Maja

UVA 10182：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=40&page=show_problem&problem=1123
GPE 考古：10551

思考邏輯：
往下：(x, y) -> (x, y+1)
往左下：(x, y) -> (x-1, y+1)
往左上：(x, y) -> (x-1, y)
往上：(x, y) -> (x, y-1)
往右上：(x, y) -> (x+1, y-1)
往右下：(x, y) -> (x+1, y)

題目範例規則：下 -> 左上 -> 上 -> 右上 -> 右下 -> 
            下 -> 下 -> 左下 -> 左上 -> 左上 -> 上 -> 上 -> 右上 -> 右上 -> 右下 -> 右下 -> 
            下 -> 下 -> 下 -> 左下 -> 左下 -> 左上
觀察到的規律 ：每個方向的移動每一輪都會多一次，從 (下*1, 左下*0, 左上*1, 上*1, 右上*1, 右下*1) 開始
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int coordinate;
    while(cin >> coordinate) {
        int x = 0, y = 0, finish = 0;
        if (coordinate != 1) {
            int i = 1, turn = 1;
            while (1) {
                // 下
                for (int j = 0; j < turn; j++) {
                    y++;
                    if (++i == coordinate) {
                        cout << x << " " << y << "\n";
                        finish = 1;
                        break;
                    }
                }
                if (finish) break;
            
                // 左下
                for (int j = 0; j < turn-1; j++) {
                    x--;
                    y++;
                    if (++i == coordinate) {
                        cout << x << " " << y << "\n";
                        finish = 1;
                        break;
                    }
                }
                if (finish) break;
                
                // 左上
                for (int j = 0; j < turn; j++) {
                    x--;
                    if (++i == coordinate) {
                        cout << x << " " << y << "\n";
                        finish = 1;
                        break;
                    }
                }
                if (finish) break;
                
                // 上
                for (int j = 0; j < turn; j++) {
                    y--;
                    if (++i == coordinate) {
                        cout << x << " " << y << "\n";
                        finish = 1;
                        break;
                    }
                }
                if (finish) break;
                
                // 右上
                for (int j = 0; j < turn; j++) {
                    x++;
                    y--;
                    if (++i == coordinate) {
                        cout << x << " " << y << "\n";
                        finish = 1;
                        break;
                    }
                }
                if (finish) break;
                
                // 右下
                for (int j = 0; j < turn; j++) {
                    x++;
                    if (++i == coordinate) {
                        cout << x << " " << y << "\n";
                        finish = 1;
                        break;
                    }
                }
                if (finish) break;
                turn++;
            }
        } else {
            cout << x << " " << y << "\n";
        }
    }
    
    return 0;
}