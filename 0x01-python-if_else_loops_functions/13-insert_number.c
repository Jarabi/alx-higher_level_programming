#include "lists.h"

listint_t *create_node(int number);

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Head of list
 * @number: Number to insert
 *
 * Return: Address of new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	if (!head)
		return (NULL);

	new_node = create_node(number);
	if (!new_node)
		return (NULL);

	if (!(*head))
	{
		*head = new_node;
		return (*head);
	}

	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	current = *head;

	while (current && current->next)
	{
		if (current->n > number)
		{
			new_node->next = current;
			*head = new_node;
			return (new_node);
		}

		if (current->next->n > number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}

	current->next = new_node;
	return (new_node);
}

/**
 * create_node - Creates new node
 * @number: Node value
 *
 * Return: Address of new node or NULL
 */
listint_t *create_node(int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	return (new_node);
}
