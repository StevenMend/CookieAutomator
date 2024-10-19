# Cookie Clicker Automation / Automatización de Cookie Clicker

## Overview / Descripción General
This project automates the gameplay of "Cookie Clicker" using Selenium, a web automation tool. The goal is to simulate clicking on a cookie to earn cookies and purchase upgrades to increase the cookies produced per second (CPS).

Este proyecto automatiza el juego "Cookie Clicker" utilizando Selenium, una herramienta de automatización web. El objetivo es simular clics en una galleta para ganar galletas y comprar mejoras que aumenten la producción de galletas por segundo (CPS).

## Features / Características
- **Automatic Cookie Clicking**: The script continuously clicks on the cookie.
- **Upgrade Purchases**: Automatically buys upgrades based on affordability and their CPS value.
- **CPS Logging**: Records cookies per second to a SQLite database every five minutes.
- **Error Handling**: Includes error handling to manage issues during execution.

- **Clics Automáticos en la Galleta**: El script hace clic continuamente en la galleta.
- **Compras de Mejoras**: Compra automáticamente mejoras basándose en su asequibilidad y su valor de CPS.
- **Registro de CPS**: Registra las galletas por segundo en una base de datos SQLite cada cinco minutos.
- **Manejo de Errores**: Incluye manejo de errores para gestionar problemas durante la ejecución.

## Requirements / Requisitos
- Python 3.x
- Selenium
- SQLite3
- Google Chrome (or any compatible web browser)

- Python 3.x
- Selenium
- SQLite3
- Google Chrome (o cualquier navegador web compatible)

## Installation / Instalación
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cookie-clicker-automation
