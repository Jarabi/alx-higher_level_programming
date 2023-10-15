#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: List to check
 *
 * Return: 0 if there is no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *walk;
	listint_t *run;

	if (!list || !list->next)
		return (0);

	walk = list->next;
	run = walk->next;

	while (run && run->next)
	{
		if (walk == run)
			return (1);
		walk = walk->next;
		run = run->next->next;
	}
	return (0);
}
