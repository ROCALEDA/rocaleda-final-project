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


## Caso 2:

Se configuran 600 requests distribuidos en rangos de cada 10 segundos

<img width="1517" alt="caso2" src="https://github.com/ROCALEDA/rocaleda-final-project/assets/78032463/370e9673-38cb-4dd9-b113-28728632d124">


