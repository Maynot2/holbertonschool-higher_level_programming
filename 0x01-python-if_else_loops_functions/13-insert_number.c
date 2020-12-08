#include "lists.h"
#include <stdio.h>

/**
  * insert_node - Inserts a node given a number.
  * @head: A pointer to pointer to listint_t.
  * @number: An int.
  *
  * Return: A pointer to the inserted node on success.
  *         NULL on failure.
  */

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

	current = *head;

	if (*head == NULL)
		*head = node;
	else if ((*head)->n > node->n)
	{
		node->next = *head;
		*head = node;
	}
	else
		while (current)
		{
			if (current->next == NULL && node->n > current->n)
			{
				current->next = node;
				break;
			}
			else if (current->n < node->n && node->n < current->next->n)
			{
				after = current->next;
				current->next = node;
				node->next = after;
			}
			current = current->next;
		}
	return (node);
}
