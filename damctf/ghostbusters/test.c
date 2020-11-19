#include <stdio.h>
#include <stdint.h>

int main()
{
	int64_t a = 0;
	int64_t b = 0;
	int64_t c = 110;

	a = scanf( "%p", &b );
	printf( "a: %d, b: %d, c: %d\n", a, b, c );
	return 0;
}
