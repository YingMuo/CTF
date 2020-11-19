#include <stdio.h>

char str[0x20] = {0};

int main()
{
	for( int i = 0; i < 0x20; i++ )
		str[i] = 'A';
	int a = 0;
	char buf[0x20] = {0};
	scanf( "%d", &a );
	printf( "%p\n", stdin );
	read( 0, buf, 0x20 );
	write( 1, buf, 0x20 );
	return 0;
}
