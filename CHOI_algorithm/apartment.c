#include <stdio.h>

int main(){
    int t;
    int i;
    int k,n;

    scanf("%d",&t);
    i = 0;

    while (i<t){
        scanf("%d",&k);
        scanf("%d",&n);

        int result = 0;
        int arr[14];

        for (int i =1; i<=n; i++){
            arr[i-1] = i;
        }
        int z = 0;
        while (z<k){
            int tmp[14] = {0};
            for (int i=1; i<=n;i++){
                result = 0;
                for (int j=0;j<i;j++){
                    result += arr[j];
                }
                tmp[i-1] = result;
            }
            for (int i =0; i<14;i++){
                arr[i] = tmp[i];
            }


            z++;
        }
        printf("%d\n",arr[n-1]);

        i++;
    }


    return (0);
}
