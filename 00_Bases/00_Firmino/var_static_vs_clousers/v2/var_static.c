#include <stdio.h>

int contador = 0;

	void soma_k(int k)
{
    static int n = 0;   
    n += k;               
	contador += 1;
    printf("Chamadas: %d\tcontador: %d\n", n, contador);
}

void nivel_5()
{
	soma_k(3);
}

void nivel_4()
{
	nivel_5();
}

void nivel_3()
{
	nivel_4();
}

void nivel_2()
{
	nivel_3();
}

void nivel_1()
{
	nivel_2();
}


int main(void) 
{
	nivel_1();
	nivel_1();
	nivel_2();
    return 0;
}
