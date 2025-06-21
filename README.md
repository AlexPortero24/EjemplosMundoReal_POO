# 🐾 Gestión de Mascotas en una Clínica Veterinaria

## 📌 Descripción

Este proyecto es un ejemplo práctico de **Programación Orientada a Objetos (POO)** que modela el funcionamiento básico de una clínica veterinaria. El sistema permite registrar **mascotas**, asociarlas a sus **dueños** y llevar un **historial de consultas médicas**.

El programa simula cómo una clínica puede organizar su información utilizando objetos, clases y relaciones entre ellos, ofreciendo una estructura clara y reutilizable del código.

## 🎯 Propósito

- Aplicar principios de POO como **clases**, **objetos**, **atributos**, **métodos** y **composición**.
- Representar situaciones del mundo real (gestión de una clínica veterinaria) en código Python.
- Organizar y consultar información de mascotas y sus dueños de forma estructurada.

## ⚙️ Funcionalidad

- Registrar dueños con nombre y número de teléfono.
- Registrar mascotas asociadas a sus dueños.
- Agregar consultas médicas con motivo y fecha.
- Mostrar información detallada de cada mascota y su dueño.
- Consultar el historial completo de visitas al veterinario.

## 🧱 Clases y POO

### `Dueño`
Representa al propietario de una mascota.
- **Atributos**: `nombre`, `telefono`
- **Métodos**: 
  - `mostrar_info()`: muestra los datos del dueño.

### `Mascota`
Representa a una mascota registrada en la clínica.
- **Atributos**: `nombre`, `especie`, `edad`, `dueño`, `consultas`
- **Métodos**:
  - `mostrar_info()`: muestra datos de la mascota y su dueño.
  - `agregar_consulta(motivo, fecha)`: agrega una consulta médica.
  - `mostrar_historial()`: muestra todas las consultas registradas.

### `Consulta`
Representa una consulta veterinaria específica.
- **Atributos**: `mascota`, `motivo`, `fecha`

## 📂 Archivo principal

- `clinica_veterinaria_v1.py`: Contiene toda la implementación del sistema y un ejemplo de uso al final del archivo.

## ▶️ Ejemplo de ejecución

El código crea un dueño llamado **Alex Portero**, una mascota **Mia (Gato)**, y dos consultas médicas. Luego, imprime toda la información registrada, demostrando cómo interactúan las clases.

---
