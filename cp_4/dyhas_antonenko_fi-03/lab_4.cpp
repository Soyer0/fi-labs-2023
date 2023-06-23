#include <iostream>
#include <string>
#include <cmath>
using namespace std;

void addone(int *mas){
  mas[0] = mas[0] + 1;
  for(int i = 0; i < 24; i++){
    if(mas[i] == 2){
      mas[i] = 0;                      ///////// функція +1
      mas[i+1] = mas[i+1] + 1;
    }
    else break;
  }
   if(mas[24] == 2) mas[24] = 0;
}

int main() {
  string v = "101010111100100000110110100010001000010011000101010110000111010100100111000011101101110000101010000010010110111011101111011011100101111000110011001011001000110000000100000111101101001111100110111000110011111010000111110011100111100011001111110010100010000110100000000011001101111111111010111000001011110100000010001011101000101111010101110111110111011110011000011001";
  int vidp[222];
  for(int i = 0; i < 222; i++){
    vidp[i] = v[i] - 48;  
  }
 
  int a = 222;
  int b = 71;
  int mas[25] = {0};

  
  for(int i = 0; i < (int) pow(2, 25); i++){
    int r = 0;
    
    int tempmas2[222] = {0};
    for (int i = 0; i < 25; i++){
      tempmas2[i] = mas[i];
    }
    
    for(int k = 0; k < 222 - 25; k++){
      if(tempmas2[k] == tempmas2[k+3]){
      tempmas2[k + 25] = 0;                        // розширюємо за L_1 вектор до довжини 222
      }
      else {tempmas2[k + 25] = 1;}
    }

    for (int i = 0; i < 222; i++){
      if(vidp[i] != tempmas2[i]){
        r++;                                      // порівнюємо з відповидним вектором
      }
    }
    if(r < 71){
      for(int i = 0; i < 25; i++){
        cout << mas[i];         // виводимо вектор і r
      }
      cout << "\t r=" << r << endl;
    }
    addone(mas);
  }
  
}