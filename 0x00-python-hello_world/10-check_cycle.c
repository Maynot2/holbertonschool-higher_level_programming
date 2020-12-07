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

	if (list == NULL || list->next == NULL)
		return (0);

	if (list->next == list)
		return (1);

	tortoise = list;
	hare = list->next;

	while (hare->next)
	{
		if (tortoise == hare)
			return (1);
		hare = hare->next->next;
		tortoise = tortoise->next;
	}
	return (0);
}
