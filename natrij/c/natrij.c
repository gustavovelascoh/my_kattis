#include <stdio.h>
#include <stdint.h>

uint16_t main(char argc, char * argv[]){

    int hi, mi, si, ho, mo, so, hd, md, sd;
    int ret, secs_i, secs_o, delta;

    ret = scanf("%d:%d:%d",&hi, &mi, &si);
    ret = scanf("%d:%d:%d",&ho, &mo, &so);
    
    if (ho < hi){
        ho = ho + 24;
    }

    secs_i = hi*3600+mi*60+si;
    secs_o = ho*3600+mo*60+so;
    
    delta = secs_o - secs_i;
    hd = delta/3600;
    md = (delta % 3600) / 60;
    sd = delta % (60);
    
    if ((hd + md + sd)  == 0){
        hd = 24;
    }
    
    printf("%02d:%02d:%02d\n",hd, md, sd);

    return 0;
}
