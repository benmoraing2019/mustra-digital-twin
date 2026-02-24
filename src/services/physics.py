import numpy as np
import json

class PhysicsService:
    def __init__(self, Da_ref, beta, kappa, gamma, theta_0, eps_divisor=1e-3):
        """
        Servicio que encapsula las ecuaciones diferenciales del CSTR.
        Totalmente desacoplado de la lógica de lectura de archivos JSON.
        """
        self.Da_ref = Da_ref
        self.beta = beta
        self.kappa = kappa
        self.gamma = gamma
        self.theta_0 = theta_0
        
        # La protección numérica ahora se inyecta directamente
        self.eps = eps_divisor

    def Da(self, theta):
        """
        Calcula el número de Damköhler efectivo.
        Fórmula optimizada: Da_ref * exp(gamma * theta / (1 + theta + eps))
        """
        exponente = (self.gamma * theta) / (1.0 + theta + self.eps)
        da = self.Da_ref * np.exp(exponente)
        return da
    
    def balance_global(self, tau, state):
        """Sistema de EDOs para scipy.integrate"""
        C, theta = state
        Da_efectivo = self.Da(theta)
        
        # Balance de Masa
        dC_dtau = 1.0 - C - (Da_efectivo * C)
        
        # Balance de Energía (Reacción Exotérmica)
        dtheta_dtau = self.theta_0 - theta + (self.beta * Da_efectivo * C) - (self.kappa * theta)
        
        return [dC_dtau, dtheta_dtau]

# --- Cómo instanciarlo usando la nueva estructura del JSON ---
if __name__ == "__main__":
    # 1. Leemos el archivo con la nueva estructura
    with open("config.json", 'r') as file:
        config_data = json.load(file)
    
    # 2. Extraemos los bloques lógicos reorganizados
    params_base = config_data["Physics_Params"]["base_case"]
    protecciones = config_data["Protections"]
    
    # 3. Instanciamos usando "desempaquetado de diccionarios" (**)
    # El **params_base asigna automáticamente cada llave del diccionario a su argumento correspondiente.
    fisica = PhysicsService(
        **params_base, 
        eps_divisor=protecciones.get("divisor", 1e-3)
    )
    
    print(f"Física instanciada con éxito.")
    print(f"Parámetros cargados -> Da_ref: {fisica.Da_ref}, theta_0: {fisica.theta_0}, kappa: {fisica.kappa}")