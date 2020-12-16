#include "lists.h"
#include <stdio.h>

/**
  * list_len - Computes the length of a single linked list.
  * @head: A pointer to the first node of the list.
  *
  * Return: The number of nodes in the list.
  *         0 if the list is empty or NULL.
  */

int list_len(listint_t *head)
{
	int c = 0;

	while (head)
	{
		c++;
		head = head->next;
	}
	return (c);
}

/**
  * get_node_at_index - Gets the node at a given index the length of a single
  * linked list.
  * @head: A pointer to the first node of the list.
  *
  * Return: The number of nodes in the list.
  *         0 if the list is empty or NULL.
  */

listint_t *get_node_at_index(listint_t *head, int idx)
{
	int index;

	if (!head)
		return (NULL);

	index = 0;
	while (head)
	{
		if (index == idx)
			return (head);
		index++;
		head = head->next;
	}
	return (NULL);
}

/**
  * is_palindrome - Tests if a single linked list is a palindrome.
  * @head: A pointer to to a pointer to the first node of the list.
  *
  * Return: 1 if the list is a palindrome.
  *         0 if the list isn't.
  */

int is_palindrome(listint_t **head)
{
	int i;
	int len;
	int last_idx;
	listint_t *node_left;
	listint_t *node_right;

	if (!head)
		return (0);

	len = list_len(*head);
	last_idx = len - 1;

	i = 0;
	while (i <= len / 2)
	{
		node_left = get_node_at_index(*head, i);
		node_right = get_node_at_index(*head, last_idx - i);
		if (node_left->n != node_right->n)
			return (0);
		i++;
	}
	return (1);
}
