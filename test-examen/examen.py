import csv                      # Para leer el archivo CSV
import json                     # Para guardar los reportes en formato JSON
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
    except ValueError:
        errors.append(f"Line {line_number}: invalid date '{date_str}'") # Error si no cumple
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
        amount = float(amount_str)   # Intento convertirlo a número decimal
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
    totals_by_customer = {}   # Diccionario para acumular totales por cliente
    totals_by_category = {}   # Diccionario para acumular totales por categoría

    # Recorro cada fila válida
    for row in valid_rows:
        c = row["customer"]
        cat = row["category"]
        amt = row["amount"]

        # TODO: convertir las lineas 70 y 71 en codigos mas idiomatico(usar mas caracteristicas del lenguaje)
        # TODO: explorar el metodo `setdefault(key, value)` 
        totals_by_customer[c] = totals_by_customer.get(c, 0) + amt  # Sumo por cliente
        totals_by_category[cat] = totals_by_category.get(cat, 0) + amt  # Sumo por categoría

    # Redondeo a 2 decimales usando dict comprehension. 
    totals_by_customer = {k: round(v, 2) for k, v in totals_by_customer.items()}
    totals_by_category = {k: round(v, 2) for k, v in totals_by_category.items()}
    
    return totals_by_customer, totals_by_category

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
    input_file = "transactions_batch_3.csv"   # Nombre del archivo CSV
    report_file = "report.json"               # Archivo donde guardo el resumen
    errors_file = "errors.log"                # Archivo donde guardo los errores

    rows = archivo(input_file)   # Cargo todas las filas del CSV

    valid_rows = []   # Lista para filas válidas
    errors = []       # Lista para los errores

    # Recorro cada fila con su número de línea (empiezo en 2 porque la 1 es el header)
    for i, row in enumerate(rows, start=2):
        valid_row = validate_row(row, i, errors) # Valido la fila
        if valid_row:
            valid_rows.append(valid_row)        # Si es válida, la agrego

    # Calculo totales
    totals_by_customer, totals_by_category = compute_totals(valid_rows)

    # Determino el cliente y la categoría top
    top_customer = pick_top(totals_by_customer)
    top_category = pick_top(totals_by_category)

    # Armo el reporte final como diccionario
    report = {
        "totals": {
            "by_customer": totals_by_customer,
            "by_category": totals_by_category,
            "transactions_count": len(valid_rows), # Cantidad de filas válidas
            "invalid_rows": len(errors)            # Cantidad de filas inválidas
        },
        "top_customer": top_customer,
        "top_category": top_category
    }

    # Escribo el reporte y los errores
    write_report(report_file, errors_file, report, errors)

    print("✅ Análisis terminado. Mirá 'report.json' y 'errors.log'")

# Ejecuto el programa principal
if __name__ == "__main__":
    main()
