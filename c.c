#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main(){

    char unit;
    char to_unit;
    double temp;

    printf("Enter a temperature unit (C, F, K): ");
    scanf(" %c", &unit);
    unit = toupper(unit);

    if (unit != 'C' && unit != 'F' && unit != 'K') {
        printf("%c is not a temperature unit", unit);
        return 1;
    }

    printf("Convert %c to what unit? ", unit);
    scanf(" %c", &to_unit);
    to_unit = toupper(to_unit);

    if (to_unit != 'C' && to_unit != 'F' && to_unit != 'K') {
        printf("%c is not a temperature unit", to_unit);
        return 1;
    }

    printf("Enter a temperature: ");
    scanf(" %lf", &temp);

    switch(unit){
        case 'C':
            switch(to_unit){
                case 'F':
                    temp = (temp * 9/5) + 32;
                    break;

                case 'K':
                    temp = temp + 273.15;
                    break;
                
                default:
                    break;
                    
            }
            break;

        case 'F':
            switch(to_unit){
                case 'C':
                    temp = (temp - 32) * 5/9;
                    break;

                case 'K':
                    temp = ((temp - 32) * 5/9) + 273.15;
                    break;
                
                default:
                    break;
            }
            break;
        
        case 'K':
            switch(to_unit){
                case 'C':
                    temp = temp - 273.15;
                    break;
                
                case 'F':
                    temp = ((temp - 273.15) * 9/5) + 32;
                    break;

                default:
                    break;
            }
            break;
        break;

        default:
            break;
    }
    printf("Converted %c to %c: %0.2lf", unit, to_unit, temp);
    return 0;
}