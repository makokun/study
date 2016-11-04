#include <avr/io.h>
#include <util/delay.h>

int main()
{
        DDRB = 0b00001000;

	while(1){
		PORTB |= 0b00001000;
		PORTB &= ~0b00001000;
		_delay_ms(1000);
	}
}

