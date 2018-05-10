#include <stdio.h>
#include <stdint.h>

uint16_t main(char argc, char * argv[]){

    int a, b, n, i;
    char sk[8];
    int ret=0;
    ret = scanf("%d",&n);

    for (i=0; i<n; i++){
        ret = scanf("%d+%d", &a, &b);
        if (ret > 0)
        {   
            printf("%d\n", a+b);
        }
        else {
            ret = scanf("%s", sk);
            printf("skipped\n");
        }
    }
    return 0;
}
