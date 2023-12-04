#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct ListNode - singly linked list
 * @data: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct ListNode {
    int data;
    struct ListNode* next;
} ListNode;

//function definitions
void push(ListNode** head, int data);
int is_palindrome(ListNode** head);
void print_list(ListNode* head);

#endif /* LISTS_H */
