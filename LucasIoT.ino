//Libs do espnow e wifi
#include <esp_now.h>
#include <Wifi.h>

//Canal usado para conexão
#define CHANNEL 1

//PInos que iremos ler (digitalRead) e enviar para os Slaves
//É importante que o código fonte dos Slaves tenha este mesmo array com os mesmos //gpios
//na mesma ordem

uintB gpios[] = {23,2};

// No setup

