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

Se configuran 100 requests a lo largo de un minuto. Aproximadamente 2 request por segundo.

<img width="1272" alt="Captura de pantalla 2023-09-24 a la(s) 21 20 04" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/3919a27a-4c79-4468-8b65-a4a7320a5158">

En este caso no se presentaron errores y las 100 solicitudes resultaron exitosas.

## Caso 2:

Se configuran 600 requests distribuidos a lo largo de un minuto. Aproximadamente 10 request por segundo.

<img width="1272" alt="Captura de pantalla 2023-09-24 a la(s) 21 21 48" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/6b21b094-43dc-430a-ac04-8903dc14ad85">


En este caso no se presentaron errores y las 600 solicitudes resultaron exitosas.

## Caso 3:

Se configuran 600 request en simultáneo.

<img width="1661" alt="Captura de pantalla 2023-09-24 a la(s) 16 32 43" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/2ff6bd69-c37a-4b73-91b7-7ce8346fcad2">

En este caso si se presentaron errores, fallaron 91 solicitudes de las 600 enviadas lo que representa un 15% app. Ya con esto sabemos que con nuestra arquitectura actual desplegada en GCP con 600 request ya comienzan aparecer errores. Un propuesta para mejorar esto es agregar un Caché para que las consultas repetitivas de este experimento ya se respondan desde la bd en memoria en vez de hacer las consultas a la base de datos. Además en este caso no hay instalada una cola que maneje las solicitudes. Por lo que si fuera el caso hay muchas posibilidades de mejora.






