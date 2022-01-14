#include <stdio.h>

int	sqrt(int nb)
{
	int i;

	i = 1;
	while (i * i <= nb)
		i++;
	return (i - 1);
}

int	is_prime(int nb)
{
	int	i;

	i = 1;
	if (nb <= 1)
		return (0);
	else if (nb == 2 || nb == 3)
		return (1);
	while (++i <= sqrt(nb))
		if (nb % i == 0)
			return (0);
	return (1);
}

void op()
{
	int	n;

	scanf("%d", &n);

}

int main()
{
	int	t;

	scanf("%d", &t);
	while (t--)
		op();
}
