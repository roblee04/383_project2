#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node {
    int arrival_time;
    int service_time;
    int priority;
    struct node* next;
} node;

node* create_job() {
    int seed = time(NULL); // always use this seed
    srand(seed); // guarantee consistency when debugging
    int arrival_time = rand() % 100; // will return num between 0 and 99
    int service_time = (rand() % 11); // will return num between 0 and 10
    if (service_time = 0) service_time += 0.1; // service_time = 0.1 .. 10
    int priority = rand() % 5;
    if (priority = 0) priority += 1; // priority between 1 .. 4

    node *new_job = (node*) malloc(sizeof(node));
    new_job->arrival_time = arrival_time;
    new_job->service_time = service_time;
    new_job->priority = priority;
    new_job->next = NULL;

    return new_job;
}

int main()
{

    // call create job 10x
    node* job = create_job();
    int a = job->arrival_time;
    int b = job->service_time;
    int c = job->priority;

    printf("%d %d %d", a, b, c);

}