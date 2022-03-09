#include <stdio.h>
int main(){
    char str[10000000]={};
    int count = 0;

    int i=0;
    while (1){

        scanf("%s",&str[i]);
        if ( !str[i] ) break;
        while (str[i]){
            i++;
        }
        count ++;
    }
    printf("%d\n",count);


    return 0;
}
