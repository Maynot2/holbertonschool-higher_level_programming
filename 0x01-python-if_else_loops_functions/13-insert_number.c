#include "lists.h"
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *after = NULL;
	listint_t *node = NULL;

	if (*head && (*head)->next)
	{
		current = *head;
		after = current->next;
		node = malloc(sizeof(listint_t));
		if (!node)
			return (NULL);
		node->n = number;
		node->next = NULL;
	}

	while(current)
	{
		if((current->n < node->n) && (after->n > node->n))
		{
			node->next = after;
			current->next = node;
		}
		if(current->n < node->n && current->next == NULL)
			current->next = node;
		current = current->next;
		if(after->next)
			after = after->next;
	}
	return (node);
}
