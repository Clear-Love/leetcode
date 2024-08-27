#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 10000

typedef struct {
    int* q[MAX_SIZE];
    int* max[MAX_SIZE];
    int q_front, q_rear;
    int max_front, max_rear;
} Checkout;

Checkout* checkoutCreate() {
    Checkout* checkout = (Checkout*)malloc(sizeof(Checkout));
    checkout->q_front = 0;
    checkout->q_rear = -1;
    checkout->max_front = 0;
    checkout->max_rear = -1;
    return checkout;
}

static inline bool isEmpty(Checkout* checkout) {
    return checkout->q_front > checkout->q_rear;
}

int checkoutGet_max(Checkout* checkout) {
    if (isEmpty(checkout)) {
        return -1;
    }
    return checkout->max[checkout->max_front];
}

void checkoutAdd(Checkout* checkout, int value) {
    checkout->q[++checkout->q_rear] = value;
    while (checkout->max_front <= checkout->max_rear && value > checkout->max[checkout->max_rear]) {
        checkout->max_rear--;
    }
    checkout->max[++checkout->max_rear] = value;
}

int checkoutRemove(Checkout* checkout) {
    if (isEmpty(checkout)) {
        return -1;
    }
    int res = checkout->q[checkout->q_front++];
    if (checkout->max_front <= checkout->max_rear && res == checkout->max[checkout->max_front]) {
        checkout->max_front++;
    }
    return res;
}

void checkoutFree(Checkout* checkout) {
    free(checkout);
}