import functools

# --- DECORADOR: Agente D ---
def agente_d(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Infiltración Universal: Soporta cualquier cantidad de *args y **kwargs
        
        # 2. Informe de Entrada
        print(f"[INFORME]: ¡Agente D infiltrando al objetivo '{func.__name__}'!")
        print(f"[INTELIGENCIA]: Equipamiento táctico (args) detectado: {args}")
        print(f"[INTELIGENCIA]: Documentos secretos (kwargs) recuperados: {kwargs}")
        
        # Ejecución de la función objetivo
        resultado = func(*args, **kwargs)
        
        # 3. Extracción del Secreto: Intercepta el resultado y lo reporta
        print(f"[EXTRACCIÓN]: Secreto interceptado con éxito -> Resultado: {resultado}")
        
        # Retorna el resultado original para no alterar el comportamiento de la función
        return resultado

    return wrapper


# --- PRUEBAS / EJEMPLO DE USO ---

print("=== PRUEBA 1: Función de transmisión de mensajes ===")
@agente_d
def transmitir_mensaje(codigo, destino, urgente=False):
    """Suma/Procesa datos o simula una acción secreta"""
    return f"Mensaje enviado a {destino} con código {codigo} (Urgente: {urgente})"

# Ejecución de prueba 1
transmitir_mensaje("X-99", "Base Alfa", urgente=True)


print("\n=== PRUEBA 2: Función de cálculo matemático ===")
@agente_d
def calcular_coordenadas(x, y, z, multiplicador=1.5):
    return (x + y + z) * multiplicador

# Ejecución de prueba 2
calcular_coordenadas(10, 20, 30, multiplicador=2.0)

# Función objetivo de prueba
@agente_d
def desactivar_bomba(codigo, tiempo_restante):
    print(f"(Ejecutando proceso interno con código {codigo}...)")
    return "'Bomba desactivada con éxito.'"

# Desplegando al Agente D sobre el objetivo
desactivar_bomba("código-azul", tiempo_restante=30)