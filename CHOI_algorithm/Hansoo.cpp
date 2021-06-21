#include <stdio.h>
int main() {
    int n,num;
    int h,t,o;
    int count = 0;

    scanf("%d",&n);

    for (int i=1;i<=n;i++){
        if (i >=100){
            num = i;
            h = num / 100;
            num = num - 100*h;

            t = num / 10;
            num = num - 10 * t;

            o = num;

            if (h-t == t-o){
                count += 1;
            }
        } else {
            count += 1;
        }
    }
    printf("%d \n",count);



    return 0;
}
