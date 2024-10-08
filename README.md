# MCD (Máximo Común Divisor) para Cuatro Números usando TDD
Este proyecto implementa un algoritmo para calcular el Máximo Común Divisor (MCD) de cuatro números enteros, utilizando el algoritmo de Euclides. Además, se sigue la metodología de Desarrollo Guiado por Pruebas (TDD) en Python, asegurando que las funciones sean probadas y validadas mediante pruebas unitarias.

# Descripción
El cálculo del MCD de cuatro números se realiza utilizando el subalgoritmo para calcular el MCD de dos números, aplicando el algoritmo de Euclides. La fórmula utilizada es:
\[
\text{MCD}(n1, n2, n3, n4) = \text{MCD}(\text{MCD}(n1, n2), \text{MCD}(n3, n4))
\]

### Funciones Implementadas:

- `mcd_dos_numeros(n1, n2)`: Calcula el MCD de dos números utilizando el **algoritmo de Euclides**.
- `mcd_cuatro_numeros(n1, n2, n3, n4)`: Calcula el MCD de cuatro números utilizando la función anterior.

## Requisitos

- **Python 3.13.0** instalado.

## Instalación

1. Clona este repositorio:
   ```bash
   https://github.com/CalderonRomero/pruebas-TDD-M-ximo-com-n-divisor-MCD-.git
