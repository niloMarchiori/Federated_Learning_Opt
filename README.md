# Fluxo do treinamento

1. Server:
    * Obtem os inputs do Modelo de Otimização
    * Obtem os valores ótimos e inicia o treinamento
    * server publica em 'minifed/selectionQueue' selecionados
    * usa a variável global MODEL_TRAINED para esperar o cliente concluir o treinamento

2. Client: 

    |callback on_message_selection() escutando 'minifed/selectionQueue'|
    * Recebe a mensagem que foi selecionado
    * Roda a calibragem do modelo
    * Publica os pesos em minifed/preAggQueue

3. Server: 

    |callback on_message_agg() escutando minifed/preAggQueue|
    * Recebe os pesos e armazena eles
    * Libera a variável MODEL_TRAINED para que o próximo client comece o trainamento

4. Server:

    |Todos os clients calibraram seus modelos|
    * Agrega-se os pesos e os publica em 'minifed/posAggQueue'
    * Espera as métricas escutando com on_message_metrics()
    
5. Client:

    |Callback on_message_agg() escutando 'minifed/posAggQueue'|
    * Recebe os pesos agregados
    * Teste o modelo e obtem as métrica**
    * Atualiza os pesos
    * Publica as métricas (id | acc | energy | selected) em 'minifed/metricsQueue'

6. Server:
    |Recebeu todas as métricas|
    * Para caso a acurácia médica global desejada foi alcançada



# To do:
    * Validação assíncrona
1. Hoje:
    * Controller store the ctts
    * Server need access to Opt_Model
    * Opt_Model consume from Controller.ctts

2. Amanha:
    * ClientSensorOpt need to mensure model/data size
    * Models and datasz need to get included in metrics

3. Indefinido:
    * Pensar numa forma de mensurar o consumo de energia desconsiderando o tempo ocioso por contra do trainemento assíncrono