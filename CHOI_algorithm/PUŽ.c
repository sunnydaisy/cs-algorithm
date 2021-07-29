#include <stdio.h>
#include <math.h>
int main(){
    int a,b,v,count;
    double x,y;
    
    scanf("%d %d %d",&a,&b,&v);
    
    x = v - b;
    y = a - b;
    
    count = (int)ceil(x/y);
    printf("%d\n",count);
    
    return 0;
}
