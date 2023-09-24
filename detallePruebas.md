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

## Caso 1:

Se configuran 100 requests en simultáneo

![set caso1](/Users/robertoparra/Desktop/caso1.png)


## Caso 2:

Se configuran 600 requests distribuidos a lo largo de un minuto

