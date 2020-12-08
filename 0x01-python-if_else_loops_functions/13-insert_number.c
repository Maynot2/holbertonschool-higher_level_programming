#include "lists.h"
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *after = NULL;
	listint_t *node = NULL;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL)
		*head = node;
	else
	{
		if ((*head)->next == NULL && node->n > (*head)->n)
		{
			(*head)->next = node;
			return (node);
		}
		current = *head;
		if (current->next)
			after = current->next;
		while (current)
		{
			if(current->n < node->n && current->next == NULL)
			{
				current->next = node;
				break;
			}
			if((current->n < node->n) && (after->n > node->n))
			{
				node->next = after;
				current->next = node;
			}
			current = current->next;
			if(after->next)
				after = after->next;
		}
	}
	return (node);
}
