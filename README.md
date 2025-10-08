---
title: "Meu Incrível Artigo"
author: "Isaac Newton"
bibliography: referencias.bib
---
# Introdução 



# Objetivo



# Fluxo do treinamento

1. Server:
    * Obtem os inputs do Modelo de Otimização
    * Obtem os valores ótimos e inicia o treinamento
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
    * Pensar numa forma de mensurar o consumo de energia desconsiderando o tempo ocioso por contra do trainemento assíncrono

# Referências


[1] Tran, N. H., Bao, W., Zomaya, A. Y., Nguyen Minh, N. H., & Hong, C. S. (2019). Federated Learning over Wireless Networks: Optimization Model Design and Analysis. International Conference on Computer Communications, 1387–1395. https://doi.org/10.1109/INFOCOM.2019.8737464


[2] Han, X., Li, J., Chen, W., Mei, Z., Wei, K., Ding, M., & Poor, H. V. (2023). Analysis and Optimization of Wireless Federated Learning with Data Heterogeneity. arXiv.Org, abs/2308.03521. https://doi.org/10.48550/arxiv.2308.03521

[3] A Novel Joint Dataset and Incentive Management Mechanism for Federated Learning Over MEC. (2022). IEEE Access, 10, 30026–30038. https://doi.org/10.1109/access.2022.3156045

[4] Kim, J., Kim, D., Lee, J., & Hwang, J.-Y. (2022). A Novel Joint Dataset and Computation Management Scheme for Energy-Efficient Federated Learning in Mobile Edge Computing. IEEE Wireless Communications Letters, 11(5), 898–902. https://doi.org/10.1109/lwc.2022.3147236