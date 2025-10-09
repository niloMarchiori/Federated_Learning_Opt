# Introdução 



# Objetivo

A ferramenta MininetFed [5] possibilita emular redes de aprendizado federado, de forma a disponibilizar um ambiente sensível ao consumo de energia. Os próprios autores da ferramenta mencionam no trabalho [6] a necessidade de desenvolver algoritmos que otimizem o consumo de energia em redes de treinamento, mas reconhecem não apresentar em si um modelo de otimização. 

Outros trabalhos ocmo [1] e [5] apresentam modelos muito bem estruturados e também métodos que atingem suas soluções ótimas. Tais trabalhos se concentram em analisar o modelo teórico, por outro lado deixam lacunas na apresentação de resultados práticos que se aproximem da eficiêna real de tais modelos de otimização.

O intúito dessa pesquisa é utilizar-se da ferramenta MininetFed para emular a rede de aprendizado federado lançando mão dos modelos de otimização no objetivo de, com essa emulação sermos, capazes de produzir dados pseudo-realísticos que possibilitem análises da eficiência dos modelos teóricos em ambientes reais.


# Fluxo da emulação de treinamento

1. Server:
    * Obtem os inputs do Modelo de Otimização
    * Obtem os valores ótimos por meio do FEDL [1] e inicia o treinamento
    * server publica em 'minifed/selectionQueue' selecionados
    * usa a variável global MODEL_TRAINED para esperar o cliente concluir o treinamento

2. Client: 

        callback on_message_selection() escutando 'minifed/selectionQueue'
    * Recebe a mensagem que foi selecionado
    * Roda a calibragem do modelo
    * Publica os pesos em minifed/preAggQueue

3. Server: 

        callback on_message_agg() escutando minifed/preAggQueue
    * Recebe os pesos e armazena eles
    * Libera a variável MODEL_TRAINED para que o próximo client comece o trainamento

4. Server:

        Todos os clients calibraram seus modelos
    * Agrega-se os pesos e os publica em 'minifed/posAggQueue'
    * Espera as métricas escutando com on_message_metrics()
    
5. Client:

        Callback on_message_agg() escutando 'minifed/posAggQueue' 
    * Recebe os pesos agregados
    * Teste o modelo e obtem as métrica**
    * Atualiza os pesos
    * Publica as métricas (id | acc | energy | selected) em 'minifed/metricsQueue'

6. Server:
        Recebeu todas as métricas 
    * Para caso a acurácia médica global desejada foi alcançada

# Implementação do modelo de otimização

(Repositório da reprodução do experimento teórico)

[https://github.com/niloMarchiori/Model_analysis]

# Problemas e próximos passos

## Problemas não resolvidos

1. As interfaces de redes dos dispositivos de redes 6LowPan não possuem Tx_Power (previsto no modelo de otimização)

2. Dispositivos com interface de rede que permitem o controlo manual de Tx_Power não possuem consumo de energia implementado
    * Segundo Ramon a implementação é simples, entretando seria necessário encontrar um modelo matemático

## Problemas sendo resolvidos
1. A falta de controle total da frequência de cpu pode ser resolvida usando o treinamento assíncrono dos clientes
* No treinamento assíncrono como será mensurado o consumo de energia?



## To do:

* [ ] Validação assíncrona

1. Em andamento:
    * Controller store the ctts
    * Server need access to Opt_Model
    * Opt_Model consume from Controller.ctts

2. Para depois:
    * ClientSensorOpt need to mensure model/data size
    * Models and datasz need to get included in metrics

3. Standy: 
    * Pensar numa forma de mensurar o consumo de energia desconsiderando o tempo ocioso por conta do trainemento assíncrono

# Referências

<a name="ref1"></a>
[1] Tran, N. H., Bao, W., Zomaya, A. Y., Nguyen Minh, N. H., & Hong, C. S. (2019). Federated Learning over Wireless Networks: Optimization Model Design and Analysis. International Conference on Computer Communications, 1387–1395. https://doi.org/10.1109/INFOCOM.2019.8737464

<a name="ref2"></a>
[2] Han, X., Li, J., Chen, W., Mei, Z., Wei, K., Ding, M., & Poor, H. V. (2023). Analysis and Optimization of Wireless Federated Learning with Data Heterogeneity. arXiv.Org, abs/2308.03521. https://doi.org/10.48550/arxiv.2308.03521

<a name="ref3"></a>
[3] A Novel Joint Dataset and Incentive Management Mechanism for Federated Learning Over MEC. (2022). IEEE Access, 10, 30026–30038. https://doi.org/10.1109/access.2022.3156045

<a name="ref4"></a>
[4] Kim, J., Kim, D., Lee, J., & Hwang, J.-Y. (2022). A Novel Joint Dataset and Computation Management Scheme for Energy-Efficient Federated Learning in Mobile Edge Computing. IEEE Wireless Communications Letters, 11(5), 898–902. https://doi.org/10.1109/lwc.2022.3147236

[5] Johann Bastos, João Batista, Ramon Fontes, Eduardo Cerqueira, Rodolfo Villaça, and Vinícius F. S. Mota. 2025. A Lightweight Emulation Framework for Energy-Aware Federated Learning. In Proceedings of the ACM SIGCOMM 2025 Posters and Demos (ACM SIGCOMM Posters and Demos '25). Association for Computing Machinery, New York, NY, USA, 130–131. https://doi.org/10.1145/3744969.3748395

[6] J. Schmitz Bastos, J. C. Batista, R. dos Reis Fontes, E. Cerqueira, R. S. Villaça, and V. F. S. Mota. " Otimizando Energia no Aprendizado Federado em Redes de Baixa potência e com Alta Taxa de Perda de Pacotes", in Anais do XLIII Simpósio Brasileiro de Redes de Computadores e Sistemas Distribuídos, Natal/RN, 2025, pp. 43-56, doi: https://doi.org/10.5753/sbrc.2025.5786.