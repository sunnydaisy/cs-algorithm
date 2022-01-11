#include <stdlib.h>

struct n_order
{
	int mNumber;
	int mStock;
	int mQuantity;
	int mPrice;
	struct n_order *next;
};
typedef struct n_order* t_order;

struct n_table
{
	int mNumber;
	t_order start;
	struct n_table *next;
};
typedef struct n_table* t_table;



t_table init_table(int mNumber)
{
	t_table table;

	table = (t_table)malloc(sizeof(struct n_table));
	if (!table)
		return (0);
	table->mNumber = mNumber;
	table->start = 0;
	table->next = 0;
	return (table);
}

t_order init_order(int mNumber)
{
	t_order order;

	order = (t_order)malloc(sizeof(struct n_order));
	if (!order)
		return (0);
	order->mNumber = mNumber;
	order->mStock = 0;
	order->mPrice = 0;
	order->mQuantity = 0;
	order->next = 0;
	return (order);
}

t_order g_order;
t_table g_table;


// 함수 구현

t_order end_node(void)
{
	t_order tmp;

	tmp = g_order;
	while (tmp->next)
		tmp = tmp->next;
	return (tmp);
}

void init()
{
	g_table = init_table(0);
	g_order = init_order(0);
}

int buy(int mNumber, int mStock, int mQuantity, int mPrice)
{
	t_order new;
	t_order tmp;
	t_order tmp_befo;

	new = init_order(mNumber);
	new->mStock = mStock;
	new->mQuantity = mQuantity;
	new->mPrice = mPrice;
	tmp = g_order;
	tmp_befo = 0;
	if (!tmp->next)
	{
		tmp->next = new;
		return (0);
	}
	while (tmp->next && tmp->mPrice <= mPrice)
	{
		tmp_befo = tmp;
		tmp = tmp->next;
	}
	if (mPrice <= tmp->mPrice)
	{
		new->next = tmp;
		tmp_befo->next = new;
	}
	else
		tmp->next = new;

	return 0;
}

int sell(int mNumber, int mStock, int mQuantity, int mPrice)
{
	return 0;
}

void cancel(int mNumber)
{
}

int bestProfit(int mStock)
{
	return 0;
}
