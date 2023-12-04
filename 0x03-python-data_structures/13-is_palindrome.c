# include "lists.h"

/**
 * This function adds a new node with the given data at the beginning of the linked list.
 * **head: A double pointer to the head of the linked list.
 * data: The data value to be stored in the new node.
*/
void push(ListNode** head, int data) {
    ListNode* new_node = (ListNode*)malloc(sizeof(ListNode));
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

/**
 * Description: This function checks if a singly linked list is a palindrome.
 * **head: A double pointer to the head of the linked list.
 * Returns 1 if it is a palindrome, and 0 if it is not.
*/
int is_palindrome(ListNode** head) {
    if (*head == NULL) {
        // An empty list is considered a palindrome
        return 1;
    }

    ListNode* slow = *head;
    ListNode* fast = *head;
    ListNode* prev_slow = *head;
    ListNode* mid = NULL;
    int is_palindrome = 1;

    // Move fast pointer to the end of the list and slow pointer to the middle
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // If the length of the list is odd, move slow pointer one step further
    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    // Reverse the second half of the list
    ListNode* second_half = slow;
    prev_slow->next = NULL;
    ListNode* prev = NULL;
    ListNode* current = second_half;
    ListNode* next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    second_half = prev;

    // Compare the first half and reversed second half of the list
    ListNode* p1 = *head;
    ListNode* p2 = second_half;
    while (p1 != NULL && p2 != NULL) {
        if (p1->data != p2->data) {
            is_palindrome = 0;
            break;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    // Reconstruct the original list by reversing the reversed second half
    prev = NULL;
    current = second_half;
    next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    second_half = prev;
    prev_slow->next = second_half;  // Connect the first half and the reversed second half

    // If the original list length was odd, connect the middle node back to the list
    if (mid != NULL) {
        prev_slow->next = mid;
        mid->next = second_half;
    }

    return is_palindrome;
}

/**
 * Description: This function prints the elements of the linked list.
 * head: A pointer to the head of the linked list.
*/
void print_list(ListNode* head) {
    ListNode* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}
