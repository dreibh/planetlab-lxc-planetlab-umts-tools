#define _XOPEN_SOURCE
#define _XOPEN_SOURCE_EXTENDED
#define _SVID_SOURCE
#define _GNU_SOURCE
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <sys/select.h>
#include <sys/resource.h>
#include <sys/mount.h>
#include <sys/vfs.h>
#include <fcntl.h>
#include <unistd.h>
#include <sched.h>
#include <stdarg.h>
#include <dirent.h>

#include <sys/file.h>
#include <errno.h>


#include "umts.h"

//#define DEBUG

int vfd0, vfd1;
//char *inf,*outf;
int i = 0;
//int c=0;

#define BUFSIZE 2048

char lineread[BUFSIZE];
char command[BUFSIZE];

char * lock_file="/var/run/umts_lock";

int ret;

char * vsys_in="/vsys/umts_backend.in";
char * vsys_out="/vsys/umts_backend.out";

fd_set set;
char lineread[BUFSIZE];

int main(int argc, char **argv, char **envp){
   
    if (argc < 2) {
   	printf("Usage: umts <cmd> [ argument ]\n");
    	exit(1);
    } else {


    	strcpy(command, argv[1]);
    
    	if (argc > 2){
		strcat(command, " ");
		strcat(command, argv[2]);
    	}

	strcat(command, "\n");

	int lock_fd=open(lock_file,O_WRONLY|O_CREAT);

	if (lock_fd==-1){
		printf("Error in creating lock file %s. Are you root of the slice?\n", lock_file);
		exit(1);
	}


	if (flock(lock_fd, LOCK_EX |  LOCK_NB)){
		if (errno == EWOULDBLOCK){
			printf("An operation is already being performed");
			close(lock_fd);
			exit(1);
		} else if (errno == EBADF){
			printf("Error in lock file: 1\n");
			close(lock_fd);
			exit(1);
		} else {
			printf("Error in lock file: 2\n");
			close(lock_fd);
			exit(1);
		}
	}

	vfd0 = open(vsys_out, O_RDONLY | O_NONBLOCK);
    	#ifdef DEBUG
    	printf("Opened %s\n", vsys_out);
    	#endif
 
    	vfd1 = open(vsys_in, O_WRONLY);
    	#ifdef DEBUG
    	printf("Opened %s\n", vsys_in);
    	#endif


    	if (vfd0 == -1 || vfd1 == -1) {
      		printf("Error opening vsys umts entry.\n");
      		exit(1);
    	}

    	write(vfd1, command, strlen(command));	
	
	FD_ZERO(&set);

	while(1){
		FD_SET(vfd0, &set);
        	ret = select(vfd0+1, &set, NULL, NULL, NULL);
		ret=read(vfd0,lineread,2048);
		if (strstr(lineread,"EOF")) break;
		//if (ret==0) break;
	        write(1,lineread,ret);
		fflush(stdout);
                FD_CLR(vfd0,&set);
	};

   	close(vfd0);
   	close(vfd1);
   
	flock(lock_fd, LOCK_UN);
	
	close(lock_fd);

   } 

   return 0;
}

