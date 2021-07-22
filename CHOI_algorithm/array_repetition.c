#include <stdio.h>
int main(){
    int count=0,num,index=0,input;
    int arr[10];
    while (count<10){
        int yes=1;
        scanf("%d",&input);
        num = input % 42;
        if (num==0) num = -1;
        /* 배열에 있는 값인지 확인 */
        int i=0;
        while (i<10){
            if(arr[i] == num) {
                /* 이미 있는 값일 때*/
                yes = 0;
                break;
            }
            i++;
        }
        if (yes) {
            arr[index] = num;
            index ++;
        }
        count ++;
    }
    printf("%d\n",index);
    return 0;
}
