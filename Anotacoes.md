
## Investigação da dependência entre frequencia e consumo:
* Existem várias fontes que modelam essa questão, em geral condizentes entre si. Inclusive: 
---
- [Burd, T.D., Brodersen, R.W. Processor design for portable systems. J VLSI Sign Process Syst Sign Image Video Technol 13, 203–221 (1996). https://doi.org/10.1007/BF01130406]


- [Vogeleer, Memmi, Jouvelot, Coelho. The Energy/Frequency Convexity Rule: Modeling and Experimental Validation on Mobile Devices. Workshop on Power and Energy Aspects of Computation, In conjunction with the 10th International Conference on Parallel Processing and Applied Mathematics (PPAM'2013), Sep 2013, Varsovie, Poland. pp 793-803, ⟨10.1007/978-3-642-55224-3_74⟩. ⟨hal-00919414⟩].
---

* Em geral a potência $P=\alpha V^2f$, em geral $V \propto f$ é definida nos trabalhos e pode ser usada para implementar a emulação de consumo no Containernet.
    * A princípio $V$ seria a tensão real, da cpu, mas no caso da ferramenta, e usado tanto $V$ quanto $I$ como valores fictícios constantes.
    * Usar $\Delta E = P(t)\Delta t$

## Alguns erros de implementação do modelo
Erro grave: encontrando "solução" fora do espaço viável para algumas configurações de entrada, notado ao tentar ajustar certas constantes e várias as seeds. 