#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if cycle are present in linked list.
 * @list: A list.
 *
 * Return: 1 if cycle found.
 *         0 if not found.
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *tortoise;

	tortoise = list;
	hare = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
