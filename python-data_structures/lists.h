#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/* Prototipos de funciones de la lista */
void print_list_integer(int *my_list, size_t size);
int element_at(int *my_list, size_t size, int idx);
void replace_in_list(int *my_list, size_t size, int idx, int element);
void print_reversed_list_integer(int *my_list, size_t size);
int *new_in_list(int *my_list, size_t size, int idx, int element);
char *no_c(char *my_string);
void print_matrix_integer(int **matrix, size_t rows, size_t cols);
void add_tuple(int *tuple_a, size_t size_a, int *tuple_b, size_t size_b, int *result);
void multiple_returns(const char *sentence, size_t *length, char *first);
int max_integer(int *my_list, size_t size);
int *divisible_by_2(int *my_list, size_t size);
void delete_at(int *my_list, size_t *size, int idx);

#endif /* LISTS_H */
