#include <stdio.h>
int sumsum(int n);
int main(){
    int n;
    int kid;
    int parent;
    int count = 0;
    scanf("%d",&n);
    int i=1;
    while (n > sumsum(i)){
        i++;
    }
    if ( i % 2 == 1){
        int index = n - sumsum(i-1);
        kid = i;
        parent = 1;
        while (count < index-1){
            kid --;
            parent ++;
            count++;
        }
    } else {
        int index = n - sumsum(i-1);
        kid = 1;
        parent = i;
        while (count < index-1){
            kid ++;
            parent --;
            count++;
        }

    }
    printf("%d/%d\n",kid,parent);
    return 0;
}
/*
    숫자를 받으면 1 + 2 + 3.. 을 받은 숫자만큼 하는 함수
 */
int sumsum(int n){

    int i = 0;
    int re = 0;
    while ( i < n){
        i++;
        re += i;
    }
    return re;
}
