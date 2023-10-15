#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Head of list
 * @number: Number to insert
 *
 * Return: Address of new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **current;
	listint_t *new_node;

	if (!head || !(*head))
		return (NULL);

	current = head;

	while (*current && (*current)->n < number)
		current = &(*current)->next;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = *current;
	*current = new_node;

	return (new_node);
}
