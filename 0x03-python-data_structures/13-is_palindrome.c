#include "lists.h"
void _reverse(listint_t **head);
int _compare_halves(listint_t *head, listint_t *mid, int len);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer of the first node
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	int i, len, result;
	listint_t *current, *mid;

	if (head == NULL || *head == NULL)
		return (1);

	current = *head;
	mid = *head;

	/* Get size of list */
	for (len = 0; current != NULL; len++)
		current = current->next;

	len /= 2;

	for (i = 1; i < len; i++)
		mid = mid->next;

	if (len % 2 != 0 && len != 1)
	{
		mid = mid->next;
		len -= 1;
	}
	_reverse(&mid);
	result = _compare_halves(*head, mid, len);
	return (result);
}

/**
 * _compare_halves - Compares two lists.
 * @head: Pointer to the head node.
 * @mid: Pointer to the middle node.
 * @len: legth of the lists.
 * Return: If the lists are the same 1. Otherwise 0.
 */
int _compare_halves(listint_t *head, listint_t *mid, int len)
{
	int i;

	if (head == NULL || mid == NULL)
		return (1);

	for (i = 0; i < len; i++)
	{
		if (head->n != mid->n)
			return (0);
		head = head->next;
		mid = mid->next;
	}
	return  (1);
}

/**
 * _reverse - Reverses a linked list
 * @head: Pointer to pointer to head of a linked list
 */
void _reverse(listint_t **head)
{
	listint_t *current, *next, *prev;

	if  (head == NULL || *head == NULL)
		return;

	current = *head;
	prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
