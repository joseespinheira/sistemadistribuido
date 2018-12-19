
#include<stdio.h>
#include<stdlib.h>
#include "mpi.h"

#define N 4

enum tags { request= 0, reply};

int my_rank;
int size;
MPI_Request send_reqs[N];
MPI_Request recv_reqs[N];
MPI_Status send_stats[N];
MPI_Status recv_stats[N];

int deferred[N];

void critical_section(){
	char *poema[] = {"Um processo qualquer executando",
			"Outro processo entrar em acao",
			"nunca dois processos entram na regiao critica",
			"a ordem depende do processo de comunicacao"};

	printf("[%d] %s\n", my_rank, poema[my_rank]);	
}

void master_job(){
	if(size<N-1)
		printf("Too few process. ");
	if(size>N)
		printf("Too much process. ");
	if((size<N-1)||(size>N)){
		printf("This program should be initialized with %d process.\n", N);
		printf("Example:\n");
		printf("mpirun -np %d ricart_agrawala\n", N);
		MPI_Finalize();
		exit(-1);
	}
	#ifdef DEBUG
	printf("Initializing %d process...\n", size);
	#endif
}

int main(int argc, char **argv){
	int i, output, input[N], who, input_buffer, replies, ticket;
	MPI_Status tmp;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
	MPI_Comm_size (MPI_COMM_WORLD, &size);

	if(my_rank == 0)
		master_job();

	for(i=0;i<N;i++) {
		input[i]=0;
		deferred[i]=0;
	}

	ticket = my_rank;
	
	/* For all others nodes, we exchange requests */
	output = ticket;
	input_buffer = 0;
	for(i=0;i<N;i++) if(i!=my_rank) {
		/* send a request (non blocking) */
		MPI_Isend(&output, 1, MPI_INT, i, request, MPI_COMM_WORLD, &send_reqs[i]);

		/* receive a request (non blocking) from anyone */
		MPI_Irecv(&input_buffer, 1, MPI_INT, MPI_ANY_SOURCE, request, MPI_COMM_WORLD, &recv_reqs[i]);

		/* Wait send and receive a request */
		MPI_Wait(&send_reqs[i],&send_stats[i]);
		MPI_Wait(&recv_reqs[i],&recv_stats[i]);

		/* Discovers who send that request and storage it */
		who = recv_stats[i].MPI_SOURCE;
		input[who] = input_buffer;
	}

	/* At this point, all nodes know all nodes tickets.*/

	/* IDEIA: reply counter, se nos temos n-1 replys, entramos na secao critica. */

	/* For all others nodes, we send and receive replies*/
	replies = 0;
	output=1;
	for(i=0;i<N;i++) if(i!=my_rank) {
		/* For those who had sent a smaller ticket, we send a reply (non blocking) */
		if (input[i] < ticket) {
			#ifdef DEBUG
			printf("[%d] sendind a reply for %d.\n", my_rank, i);			
			#endif
			MPI_Isend(&output, 1, MPI_INT, i, reply, MPI_COMM_WORLD, &send_reqs[replies]);
			replies++;
		} else {
		/* For those who had sent a bigger ticket, we put him in the deferred list */
			deferred[i] = 1;
		}
		
		/* We wait (blocking) for an reply (we need N replies to exits this loop) */
		MPI_Recv(&input_buffer, 1, MPI_INT, MPI_ANY_SOURCE, reply, MPI_COMM_WORLD, &tmp);
		#ifdef DEBUG
		printf("[%d] Received a reply.\n", my_rank);
		#endif
	}

	/* Wait those replies we sent */
	MPI_Waitall(replies, send_reqs, send_stats);

	/* Critical Section */
	critical_section();

	/* For each one in deferred list, we send (blocking) a reply */
	for(i=0;i<N;i++) if(deferred[i]==1) {
		#ifdef DEBUG
		printf("[%d] sendind a reply for %d.\n", my_rank, i);
		#endif
		MPI_Send(&output, 1, MPI_INT, i, reply, MPI_COMM_WORLD);
	}
	#ifdef DEBUG
	printf("[%d] end...\n", my_rank);
	#endif

	MPI_Finalize();
}
