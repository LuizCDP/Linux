@echo off
setlocal EnableDelayedExpansion

:: Limpa a tela
cls

color 0A

echo Luiz - Lunix
echo Loading...
echo.

:: Animação de barra de progresso
set "bar="
for %%i in (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20) do (
    set "bar=!bar!#"
    cls
    echo Lunix
    echo by luiz
    echo.
    echo Loading...
    echo [!bar!]
    ping -n 1 localhost >nul
)

echo.
password.pyw