# tp-integracion-continua 

![CI/CD Pipeline](https://github.com/irinazibekman/tp-integracion-continua/actions/workflows/ci.yml/badge.svg)

Calculadora en Python con entorno de integración y entrega continua usando GitHub Actions.

## Funciones disponibles
- `sumar(a, b)`
- `restar(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)`

## Cómo correr las pruebas localmente
```bash
pip install -r requirements.txt
pytest tests/ -v
```