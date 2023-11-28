#include "lists.h"

/**
 * check_cycle - function that checks if a SLL has
 * a cycle in it
 * @list: pointer to the list
 * Return: 1 if there is a cycle,
 * 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
        fast = fast->next->next;

        if(slow != fast){
            return (0);
        }
	}

	return (1);
}
