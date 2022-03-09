#include <stdio.h>

int main() {
    int max, min, input, n;

    scanf("%d", &n);

    scanf("%d", &input);
    max = input;
    min = input;
    for (int i = 1; i < n; ++i) {
        scanf("%d", &input);
        if (max < input) {
            max = input;
        }
        if (min > input) {
            min = input;
        }
    }

    printf("%d %d\n", min, max);

    return 0;
}
