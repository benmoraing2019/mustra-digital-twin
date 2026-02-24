import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from src.services.physics import PhysicsService
from src.services.config_manager import ConfigManager


class SimulationService:
    def __init__(self, physics_service: PhysicsService, simulation_settings:ConfigManager):
        """
        Recibe la física y su diccionario exclusivo de configuración.
        """
        self.physics = physics_service
        self.settings = simulation_settings

    def run_simulation(self, C_init, theta_init):
        """Ejecuta la simulación usando los valores del diccionario."""
        
        # Extraemos los valores del diccionario inyectado
        tau_start, tau_final = self.settings["tau_span"]
        num_points = self.settings["num_points"]
        metodo = self.settings["solver_method"]
        
        t_span = (tau_start, tau_final)
        y0 = [C_init, theta_init]
        t_eval = np.linspace(tau_start, tau_final, num_points)

        solucion = solve_ivp(
            fun=self.physics.balance_global,
            t_span=t_span,
            y0=y0,
            t_eval=t_eval,
            method=metodo
        )

        df_resultados = pd.DataFrame({
            'tau': solucion.t,
            'Concentracion_C': solucion.y[0],
            'Temperatura_theta': solucion.y[1]
        })

        return df_resultados