import json

class ConfigManager:
    def __init__(self, filepath="src/common/config.json"):
        """Lee el archivo JSON una sola vez al inicializar la aplicación."""
        with open(filepath, 'r') as file:
            self._config = json.load(file)
            
    def get_physics_base_case(self):
        """Retorna el diccionario con los parámetros físicos nominales."""
        return self._config["Physics_Params"]["base_case"]
        
    def get_physics_ranges(self):
        """Retorna el diccionario con los rangos para generar datos sintéticos."""
        return self._config["Physics_Params"]["ranges"]
        
    def get_initial_conditions(self):
        """Retorna las condiciones iniciales de C' y theta."""
        return self._config["Initial_Conditions"]["base_case"]

    def get_simulation_settings(self):
        """Retorna SOLO el diccionario de configuración del solver."""
        return self._config["Simulation_Settings"]
        
    def get_protections(self):
        return self._config["Protections"]