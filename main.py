# main.py
# Proyecto: Generador Seguro de Contraseñas
# Asignatura: Lógica de Programación

import secrets
import string

def mostrar_menu():
    print("\n" + "="*41)
    print("   GENERADOR DE CONTRASEÑAS SEGURAS    ")
    print("="*41)
    print("1. Generar nueva contraseña")
    print("2. Salir")
    print("="*41)

def generar_contrasena(longitud, mayus, nums, esp):
    caracteres = string.ascii_lowercase
    if mayus:
        caracteres += string.ascii_uppercase
    if nums:
        caracteres += string.digits
    if esp:
        caracteres += string.punctuation

    if not caracteres:
        return "Error en los parámetros."

    contrasena_final = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena_final

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-2): ")
        
        if opcion == "1":
            try:
                longitud = int(input("\nIngrese la longitud de la contraseña (mínimo 8): "))
                if longitud < 8:
                    print("La longitud mínima debe ser de 8 caracteres.")
                    continue
                
                incluir_mayus = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
                incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
                incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'
                
                password_segura = generar_contrasena(longitud, incluir_mayus, incluir_numeros, incluir_especiales)
                
                print("\n" + "*"*41)
                print(f" Tu contraseña generada es: {password_segura}")
                print("*"*41)
                
            except ValueError:
                print("Error: Ingrese un número válido.")
                
        elif opcion == "2":
            print("\nSaliendo del sistema de seguridad. ¡Gracias por usar nuestro servicio!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()