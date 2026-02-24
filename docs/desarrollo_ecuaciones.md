# Aqui el desarrollo matemático del modelo que se ocupara para el digital twins

## Consideraciones iniciales
- Se considera una reacción del tipo $A \rightarrow B$
- La ecuación de la reacción viene dada por $kC_{A}$
- Se trabajara con valores adminesionales para poder escalar resultados:
    * $C_{A} = C'*C_{A}$
    * $t = \tau * \tau_{res}$
    * $\tau_{res} = \frac{V}{q}$
    * $T = T_{ref} \left(1 + \theta \right)$
- Se considera que la temperatura de referencia es la tempertarura del refrigerante del reactor

## Ecuaciones de modelamiento:

Ecuacion de balance de masa:
$$ \frac{dC_{A}}{dt} = \frac{q}{V}\left( C_{A0} - C_{A} \right) - kC_{A}$$

Ecuación de balance de energía:

$$\frac{dT}{dt} = \frac{q}{V}(T_0 - T) + \frac{-\Delta H_{rxn}}{\rho C_p}kC_A - \frac{UA}{V\rho C_p}(T - T_c)$$

Ecuacuión de Arrhenius:

$$ k = A*e^{\frac{-E_{a}}{RT}} $$

## Ecuaciones adimensionadas:

Ecuación balance de masa:

$$\frac{dC'}{d\tau} = 1 - C' - Da_0 \exp\left(\frac{-\gamma}{1+\theta}\right) C'$$

Ecuación balance de energía:

$$\frac{d\theta}{d\tau} = \theta_0 - \theta + \beta Da_0 \exp\left(\frac{-\gamma}{1+\theta}\right) C' - \kappa \theta$$

Ecuación de arrhenius:
$$Da(\theta) = Da_0 \exp\left(\frac{-\gamma}{1+\theta}\right)$$


## Rangos Típicos y Definiciones de Variables Adimensionales (CSTR Exotérmico)

| Parámetro | Símbolo | Fórmula de Origen | Rango Típico | Significado Físico y Notas de Diseño |
| :--- | :---: | :---: | :---: | :--- |
| **Concentración** | $C'$ | $C' = \frac{C_A}{C_{A0}}$ | 0 a 1 | Fracción de reactivo remanente. 1 significa reactor lleno de reactivo puro; 0 significa conversión del 100%. |
| **Temperatura** | $\theta$ | $\theta = \frac{T - T_{ref}}{T_{ref}}$ | 0 a 2 | Típicamente no supera el valor de 1 o 2 en fase líquida para evitar ebullición. Un $\theta$ muy alto indica descontrol térmico. |
| **Tiempo** | $\tau$ | $\tau = \frac{t}{\tau_{res}}$ | 0 a 10 | Representa cuántas veces se ha renovado el volumen ($\tau_{res} = V/q$). El estado estacionario suele alcanzarse entre $\tau = 3$ y $5$. |
| **Energía de Activación** | $\gamma$ | $\gamma = \frac{E_a}{R T_{ref}}$ | 10 a 40 | Mide qué tan sensible es la reacción a los cambios de temperatura. Valores altos (> 30) disparan la reacción con poco calor. |
| **Calor Adiabático** | $\beta$ | $\beta = \frac{-\Delta H C_{A0}}{\rho C_p T_{ref}}$ | 0.1 a 1.0 | Representa cuánto subiría la temperatura si el reactor estuviera aislado. Valores > 0.5 requieren enfriamiento robusto. |
| **Enfriamiento** | $\kappa$ | $\kappa = \frac{U A \tau_{res}}{V \rho C_p}$ | 0 a 5 | $\kappa = 0$ es un reactor adiabático. Valores entre 1 y 3 son comunes. $\kappa > 5$ aproxima a un comportamiento isotérmico. |
| **Damköhler (Pre-exp)** | $Da_0$ | $Da_0 = k_0 \tau_{res}$ | $10^6$ a $10^{15}$ | Número gigantesco para compensar el término de Arrhenius. Representa la velocidad teórica máxima a temperatura infinita. |
| **Damköhler (Efectivo)** | $Da_{ref}$ | $Da_{ref} = Da_0 \exp(-\gamma)$ | 0.01 a 10 | La velocidad real de reacción en $T_{ref}$. Si ronda entre 0.1 y 10, la reacción compite a la par con el flujo de entrada/salida. |