#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	
	for( int o = 0; o < 100; o++ )
	{
		srand( time(0) - o );
	for( int i = 0; i < 30; i++ )
	{
		printf( "%d,", rand() & 0xf );
	}
	printf( "\n" );
	}
	return 0;
}
