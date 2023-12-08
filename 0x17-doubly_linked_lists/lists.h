#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * @dlistint_s:  structure
 * @n : integer value
 * @prev: pointer to previous
 * @next: pointer to next
*/
typedef struct dlistint_s
{
    int n;
    struct dlistint_s *prev;
    struct dlistint_s *next;
} dlistint_t;

#endif
