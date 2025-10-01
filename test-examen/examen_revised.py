import csv                      # Para leer el archivo CSV
import json                     # Para guardar los reportes en formato JSON
import math

from collections import defaultdict
from datetime import datetime   # Para validar y manejar fechas

# Función para abrir y leer el archivo CSV
def archivo(nombre):    
    try:
        # Abro el archivo en modo lectura, con UTF-8 
        with open(nombre, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)   # DictReader convierte cada fila en un diccionario
            return [row for row in reader]   # Paso todas las filas a una lista          
    except FileNotFoundError:
        print("no está el archivo")          # Aviso si no se encuentra el archivo
        return []                            # Devuelvo lista vacía si no existe
    except Exception as e:
        print(f"error al leer el archivo : {e}")  # Cualquier otro error lo muestro
        return []

# Función para validar cada fila
def validate_row(row, line_number, errors):
    date_str = row.get("date", "").strip()       # Saco la fecha y elimino espacios
    customer = row.get("customer", "").strip()   # Saco el cliente
    category_val = row.get("category", "").strip() # Saco la categoría
    amount_str = row.get("amount", "").strip()   # Saco el monto

    # Validar fecha
    try:
        datetime.strptime(date_str, "%Y-%m-%d")  # Compruebo si tiene formato válido
    except ValueError as e:
        errors.append(f"Line {line_number}: invalid date '{e}'") # Error si no cumple
        return None

    # Validar cliente
    if not customer:
        errors.append(f"Line {line_number}: missing customer") # Error si está vacío
        return None

    # Validar categoría
    if not category_val:
        errors.append(f"Line {line_number}: missing category") # Error si falta
        return None

    # Validar monto
    try:
        amount = float(amount_str)
        if math.isnan(amount):
            raise ValueError("amount is NaN")
        elif amount < 0 or amount > 1e5:
            raise ValueError("amount cannot be negative")
        
    except ValueError:
        errors.append(f"Line {line_number}: invalid amount '{amount_str}'") # Error si no es numérico
        return None

    # Si todo está bien, devuelvo la fila lista
    return {
        "date": date_str,
        "customer": customer,
        "category": category_val,
        "amount": amount
    }

# Función para calcular totales
def compute_totals(valid_rows):
    totals_by_customer = defaultdict(float)   # Diccionario para acumular totales por cliente
    totals_by_category = defaultdict(float)   # Diccionario para acumular totales por categoría

    # Recorro cada fila válida
    for row in valid_rows:
        amount = row["amount"]
        totals_by_customer[row["customer"]] += amount
        totals_by_category[row["category"]] += amount
    
    # Redondea a parte para evitar decimales largos por acumulación
    totals_by_customer = {k: round(v, 2) for k, v in totals_by_customer.items()}
    totals_by_category = {k: round(v, 2) for k, v in totals_by_category.items()}

    return dict(totals_by_customer), dict(totals_by_category)

# Función para devolver el cliente/categoría con mayor gasto
def pick_top(totals_dict):
    if not totals_dict:    # Si está vacío devuelvo None
        return None
    return max(totals_dict, key=totals_dict.get) # Devuelvo la clave con el valor máximo

# Función para escribir el reporte y los errores en archivos
def write_report(report_filename, error_filename, report_data, errors):
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4) # Escribo el JSON con indentación
    except Exception as e:
        print(f"⚠️ Error al escribir el reporte: {e}")

    try:
        with open(error_filename, "w", encoding="utf-8") as f:
            for err in errors:
                f.write(err + "\n") # Escribo cada error en una línea
    except Exception as e:
        print(f"Error al escribir el log de errores: {e}")

# Función principal
def main():
    input_file = "test-examen/transactions_batch_3.csv"   # Nombre del archivo CSV
    report_file = "report_revised.json"               # Archivo donde guardo el resumen
    errors_file = "errors_revised.log"                # Archivo donde guardo los errores

    rows = archivo(input_file)   # Cargo todas las filas del CSV

    valid_rows = []   # Lista para filas válidas
    errors = []       # Lista para los errores

    # Recorro cada fila con su número de línea (empiezo en 2 porque la 1 es el header)
    for i, row in enumerate(rows, start=2):
        valid_row = validate_row(row, i, errors) # Valido la fila
        if valid_row:
            valid_rows.append(valid_row)        # Si es válida, la agrego
    
    print(f"Valid rows: {valid_rows}, Errors: {len(errors)}")
    if not valid_rows:
        print("No valid rows to process.")
        # FIXME: Por alguna razon, errors no se escribe si no hay filas validas
        write_report(report_file, errors_file, {}, errors)
        return

    # Calculo totales
    totals_by_customer, totals_by_category = compute_totals(valid_rows)

    # Armo el reporte final como diccionario
    report = {
        "totals": {
            "by_customer": totals_by_customer,
            "by_category": totals_by_category,
            "transactions_count": len(valid_rows), # Cantidad de filas válidas
            "invalid_rows": len(errors)            # Cantidad de filas inválidas
        },
        "top_customer": pick_top(totals_by_customer),
        "top_category": pick_top(totals_by_category)
    }

    # Escribo el reporte y los errores
    write_report(report_file, errors_file, report, errors)

    print("✅ Análisis terminado. Mirá 'report.json' y 'errors.log'")

# Ejecuto el programa principal
if __name__ == "__main__":
    main()
