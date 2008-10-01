all: umts

umts: umts.c umts.h
	gcc -g umts.c -o umts

clean:
	rm -f umts  *~   
