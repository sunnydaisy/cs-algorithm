#include <stdio.h>
int check(int *arr, int index, int num);
int main(){
    int num;
    int arr[10]={};
    int answer = 0;


    /* 배열의 원소 넣기
     배열은 배열 원소에 있지 않은 값이면 넣고 만약 이미 있는 원소면 넣지 않는다.
     */
    for (int i=0;i<10;i++){
        scanf("%d",&num);
        num = num % 42;
        if (num == 0) num = -1;
        if (check(arr, i, num)){
            arr[i] = num;
            answer ++;
        }
    }

    printf("%d",answer);


    return 0;
}

/* 이미 있던 원소인지 확인하는 함수
    처음 보는 원소이면 1을 리턴
    이미 배열안에 있는 원소면 0을 리턴
*/

int check(int *arr, int index, int num){
    int i=0;
    while (i<index){
        if (arr[i] == num){
            return 0;
        }
        i++;
    }
    return 1;
}
