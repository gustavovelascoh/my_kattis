#include <stdio.h>
#include <stdint.h>
#include <math.h>

uint16_t main(char argc, char * argv[]){
    
    int n, i;
    int b,e,s=0;
    
    scanf("%d",&n);

    for (i=0; i<n; i++){

        scanf("%d",&b);
        e = b % 10;
        b = b/10;
        s+=(int)pow(b,e);
    }
    
    printf("%d\n", s);
    return 0;
}
