#include "lists.h"

/**
*insert_node - this function inserts a node in a sorted manner
*@head: the head node
* @number: the number to be inserted
* Description: returns a pointer to the new node
* Return: returns a pointer to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *new_node, *current;
	listint_t *next;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number, new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	current = *head;
	if (number <= current->n)
	{
		new_node->next = current, *head = new_node;
		return (*head);
	}
	if (number > current->n && !current->next)
	{
		current->next = new_node;
		return (new_node);
	}
	next = current->next;
	while (current)
	{
		if (!next)
			current->next = new_node, flag = 1;
		else if (next->n == number)
			current->next = new_node, new_node->next = next, flag = 1;
		else if (next->n > number && current->n < number)
			current->next = new_node, new_node->next = next, flag = 1;
		if (flag)
			break;
		next = next->next, current = current->next;
	}
	return (new_node);
}
