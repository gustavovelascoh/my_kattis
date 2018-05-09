#include <stdio.h>
#include <stdint.h>

uint16_t main(char argc, char * argv[]){

    int r1, s;
    scanf("%d %d", &r1, &s);

    printf("%d\n", 2*s-r1);    

    return 0;
}
