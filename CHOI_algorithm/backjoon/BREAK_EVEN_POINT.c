#include <stdio.h>
int solution(int a, int b, int c);
int main(){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);

    printf("%d\n",solution(a, b, c));


    return 0;
}

int solution(int a, int b, int c){
    int count;
    if (c < 1 + b ) return  -1;
    count = (int)(a / (c -b));
    return count + 1 ;
}
