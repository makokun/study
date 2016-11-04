all: test.c makefile
	avr-gcc -O2 -mmcu=attiny85 -DF_CPU=1000000UL -c -o test.o test.c
	avr-gcc -O2 -mmcu=attiny85 test.o -o test
	avr-objcopy -j .text -j .data -O ihex test test.hex

clean:
	rm test.o test test.hex

