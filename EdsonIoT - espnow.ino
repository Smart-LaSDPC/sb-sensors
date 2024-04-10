\\ espnow - edson magno da silva

//Libs do espnow e wifi
#include <esp_now.h>
#include <Wifi.h>

//Canal usado para conexão
#define CHANNEL 1

//Pinos que iremos ler (digitalRead) e enviar para os Slaves
//É importante que o código fonte dos Slaves tenha este mesmo array com os mesmos //gpios
//na mesma ordem

uint8_t gpios[] = {23,2};

// No setup iremos calcular a quantidade de pinos e colocar nesta variavel,
//assim não precisamos trocar aqui toda vez que mudarmos a quantidade de pinos,
//tudo é calculado no setup

int gpioCount;
//Mac Adress dos slaves para os quais iremos enviar a leitura
//Se quiser enviar para todos os Slaves utilize apenas o endereço de broadcast {0xFF, OxFF, OxFF, 0xFF, 0xFF, 0xFF}
//Se quiser enviar para ESPs especificos coloque o Mac Adress (obtido atraves

uint8_t macSlaves[][6] = {
//Se enviar para ESPs especificos, coloque cada endereço separado por virgula
//{Ox24, OxOA, OxC4, OxOE, Ox3F, OxD1},{Ox24, OxOA, OxC4, OxOE, Ox4E, OxC3}
// Se for enviar para todos, apenas deixe o endereço de broadcast {OxFF,OxFF,OxFF,OxFFOxFF}
{OxFF,OxFF,OxFF,OxFFOxFF}
};
          
void setup() {
Serial.begin(115200);
//cálculo do tamanho do array de gpios que serão lidos como o digitalRead
//sizeof(gpios) retorna a quantidade de bytes que o array gpios aponta
//Sabenos que todos os elementos do array são do tipo uint8_t possui
//Sendo assim para saber quantos elementos o array possui
//fazendo a divisão entre a qauntidade total de bytes do array e quantos
//bytes cada elemento possui

gpioCount = sizeof(gpios)/sizeof(uint8_t);

//Colocamos o ESP em modo station

Wifi.mode(WIFI_STA);

//Mostramos no monitor Serial o MAc Adress deste ESP qaundo em modo station

Serial.print("Mac Adress in Station:");
Serial.println(WiFi.macAdress());

//Chama a função que inicializa o  ESPNow

IniESPNow();

//Cálculo do tamanho do array com os mac adress dos slaves
//sizeof(macSlaves) retorna a quantidade de bytes que o array macSlaves aponta
//Sabemos que cada mac adress é um array de 6 posições e 
//cada posição possui sizeof(unit8_t) bytes, então 
//a quantidade de slaves e a divisão da quantidade de bytes
//total do array pela quantidade de posições e o resultado
//dessa divisão dividimos novamente por quantos bytes cada posição possui

int slavesCount = sizeof(macSlaves)/6/sizeof(unit8)t);

//Para cada slave

for(int i=0;i<slavesCount;i++) {
//Criamos uma variavel que ira guardar as informações do slave
esp_now_peer_info_t slave;
//informamos o canal
slave channel = CHANNEL;
//0 para não usar criptografia ou 1 para usar
slave.encrypt = 0;
//copia o endereço do array para a estrutura
memcpy(slave.peer_addr, macSlaves[i],sideof(macSlaves[i]));
//adicionar o slave
esp_now_add_peer(&slave);
}

//Registra o calback que nos informara sobre o status do envio
// A função que sera executada é OnDataSent e está declarada mais abaixo
esp_now_register_send_cb(DataSent);

/Para cada pino que está no array gpios

for(int i=0; i<gpioCount;i++){
//colocamos em modo de leitura
pinMode(gpios[i], INPUT);
}

//chama a função send

send();
}



   


