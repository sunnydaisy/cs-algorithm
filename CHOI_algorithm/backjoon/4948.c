#include <stdio.h>

int	ft_sqrt(int nb)
{
	int	i;

	if (nb <= 0)
		return (0);
	i = 1;
	while (i * i < nb)
		i++;
	return (i);
}

int is_prim(int n)
{
	if (n <= 1)
		return (0);
	else if (n == 2 || n == 3)
		return (1);
	else if (n % 2 == 0)
		return (0);
	for (int i = 2; i <= ft_sqrt(n); i++)
	{
		if (n % i == 0)
			return (0);
	}
	return (1);
}

int ct_prim(int n)
{
	int	i;
	int	ret;

	i = n + 1;
	ret = 0;
	while (i <= 2 * n)
	{
		if (is_prim(i))
			ret ++;
		i++;
	}
	return (ret);
}

int main()
{
	int n;

	n = 0;
	while (1)
	{
		scanf("%d", &n);
		if (n == 0)
			return (0);
		printf("%d\n", ct_prim(n));
	}
	return (0);
}
