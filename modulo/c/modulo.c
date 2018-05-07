#include <stdio.h>
#include <stdint.h>

uint16_t main(char argc, char * argv[]){

    int list[42] = {0};
    int i;
    int number, mod;
    int total=0;

    for (i=0; i< 10; i++){
        scanf("%d", &number);
        
        mod = number % 42;
        if (!list[mod]){
            list[mod]=1;
            total=total+1;
//            printf("m: %d, n: %d, tot: %d\n", mod, number, total);
        }
//        printf("n: %d\n", number);    
    }

    printf("%d\n", total);    

    return 0;
}
