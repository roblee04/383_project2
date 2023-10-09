#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// code for creating x amount of jobs using x seed
// each job is stored as a node
// all jobs are stored in an array

typedef struct node {
    int arrival_time;
    int service_time;
    int priority;
    struct node* next_job;
} node;

void create_job(node* jobs[], int size, int seed) {
    
    seed = time(NULL); // always use this seed
    srand(seed); // guarantee consistency when debugging

    for(int i = 0; i < size; i++) {
        int arrival_time = rand() % 100; // will return num between 0 and 99
        int service_time = (rand() % 10) + 1; // will return num between 1 and 10
        int priority = rand() % 4 + 1; // will return num between 1 and 4

        node *new_job = (node*) malloc(sizeof(node));
        new_job->arrival_time = arrival_time;
        new_job->service_time = service_time;
        new_job->priority = priority;
        new_job->next = NULL;
        jobs[i] = new_job;
    }
    
}

int main()
{
    int size = 10;
    node* jobs[size];
    int seed = 42069;
    // parameters: 
    //     jobs = array to insert nodes into
    //     size of array = 10
    //     seed = 2, can be any integer
    create_job(jobs, size, seed);

    // print out all values
    for (int i; i < size; i ++) {
        node* job = jobs[i];
        int a = job->arrival_time;
        int b = job->service_time;
        int c = job->priority;
        printf("%d %d %d \n", a, b, c);
    }

}