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
    // service time is an int, so you cannot change it to 0.1, for now, just treat it as such
    
    // if(service_time == 0) {
    //     printf("1 \n");
    //     service_time += 0.1; // service_time = 0.1 .. 10
    //     printf("3 %d\n", service_time);
    // }
    int priority = rand() % 4 + 1; // more equal approach

    // if (priority == 0) priority += 1; // priority between 1 .. 4
    // unequal

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

    printf("%d %d %d \n", a, b, c);

}