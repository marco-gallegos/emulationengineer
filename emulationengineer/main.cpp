/*
@Author: Marco A. Gallegos
@Date: 2020/10/15
@Version: gcc 10.2.1
@Description:
    determina el numero mas pequeño de una lista no mayor a 2 y menor a 5 elementos
    guarda en un archivo el menor y la lista de numeros
*/
#include <iostream>
#include <list>
#include <fstream>


using namespace std;


int main()
{
    list<int> numeros_locos;
    list<int>::iterator iterador_loco;

    int contador_nums = 0;
    int input = 0;
    bool continuar = true;
    ofstream fs("resultC.txt");

    cout<<"dame minimo 2 numeros o maximo 5"<< endl;
    do{
        cout<<"dame un numero positivo o uno negativo para salir : ";
        cin>>input;

        if(input >= 0 && numeros_locos.size()<5){
            numeros_locos.push_back(input);
        }

        contador_nums = numeros_locos.size();
        if(contador_nums>=5 || (input<0 && contador_nums>=2)){
            continuar = false;
        }
    }while(contador_nums<2 or continuar);

    numeros_locos.sort();

    cout<<"el menor es el numero: "<<numeros_locos.front();
    fs<<"el menor es el numero;"<<numeros_locos.front()<<endl;
    fs<<"lista de numeros"<<endl;

    iterador_loco = numeros_locos.begin();

    while(iterador_loco != numeros_locos.end()){
        fs << *iterador_loco <<",";
        iterador_loco++;
    }
    fs << endl;
    fs.close();

    return 0;
}
