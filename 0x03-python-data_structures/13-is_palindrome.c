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
	if (len == 0)
		return (1);
	last_idx = len - 1;

	node_left = *head;
	i = 0;
	while (i < len / 2)
	{
		node_right = get_node_at_index(node_left, last_idx - (i * 2));
		if (node_left->n != node_right->n)
			return (0);
		node_left = node_left->next;
		i++;
	}
	return (1);
}
