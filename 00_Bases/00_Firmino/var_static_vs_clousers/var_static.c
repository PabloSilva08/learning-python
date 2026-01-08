#include <stdio.h>


	void soma_k(int k)
{
    static int n = 0;   
    n += k;               
    printf("Chamadas: %d\n", n);
}

void nivel1()
{
	soma_k(3);
}

void nivel3()
{
	soma_k(5);
}

void nivel2()
{
	nivel3();
}


int main(void) 
{
	nivel1();
	nivel2();
    return 0;
}
