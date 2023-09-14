# Instrucciones Jmeter

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

## Crear un plan de pruebas

1. Click derecho en Test Plan
2. Add > Threads (Users) > Thread Group
3. Click derecho en Thread Group
4. Add > Sampler > HTTP Request

