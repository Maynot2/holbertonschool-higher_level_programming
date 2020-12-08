#include "lists.h"
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *after = NULL;
	listint_t *node = NULL;

	if (!head)
		return (NULL);
	
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head)
		current = *head;

	if ((*head)->next)
		after = current->next;

	while(current)
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

	if (*head == NULL)
		*head = node;

	return (node);
}
