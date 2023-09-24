# Configuraciones Jmeter

## Instalación Jmeter en MacOs

Revisar Java instalado

```bash
java -version
#brew install openjdk@11
#export JAVA_HOME=$(/usr/libexec/java_home -v 11)
```

Instalar JMeter usando brew

```bash
brew install jmeter
```

## Ejecutar

Desde la terminal

```bash
jmeter
```

## Crear el plan de pruebas

1. Click derecho en Test Plan
2. Add > Threads (Users) > Thread Group
3. Click derecho en Thread Group
4. Add > Sampler > HTTP Request

Se configura el endpoint de consulta y las condiciones de filtrado

<img width="1670" alt="rutas" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/44b78891-23a2-47f2-a94e-5e1394827b25">


## Caso 1:

Se configuran 100 requests en simultáneo

<img width="1517" alt="caso1" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/fc0542c2-0095-479d-8702-89f6c56720e5">

En este caso no se presentaron errores y las 100 solicitudes resultaron exitosas.

## Caso 2:

Se configuran 600 requests distribuidos en rangos de cada 10 segundos, es decir 60 usuarios por segundo.

<img width="1517" alt="caso2" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/370e9673-38cb-4dd9-b113-28728632d124">

En este caso no se presentaron errores y las 600 solicitudes resultaron exitosas, es un caso menos estresante que el caso 1.

## Caso 3:

Se configuran 600 request distribuidos a lo largo de 60 segundos, es decir 10 usuarios por segundo.

<img width="1661" alt="Captura de pantalla 2023-09-24 a la(s) 16 32 00" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/db6c3db6-2952-4e87-9fae-7b11acf83804">

En este caso no se presentaron errores y las 600 solicitudes resultaron exitosas, es un caso menos estresante que el caso 1.

## Caso 4:

Se configuran 600 request en simultáneo.

<img width="1661" alt="Captura de pantalla 2023-09-24 a la(s) 16 32 43" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/2ff6bd69-c37a-4b73-91b7-7ce8346fcad2">

En este caso si se presentaron errores, fallaron 20 solicitudes de las 600 enviadas lo que representa un 3.33% app. Ya con esto sabemos que con nuestra arquitectura actual desplegada en GCP con 600 request ya comienzan aparecer errores. Un propuesta para mejorar esto es agregar un Caché para que las consultas repetitivas de este experimento ya se respondan desde la bd en memoria en vez de hacer las consultas a la base de datos.

<img width="908" alt="Captura de pantalla 2023-09-24 a la(s) 16 40 00" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/5a81f7cd-4959-47f3-8904-ef7cf025e52d">






