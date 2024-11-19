@echo off

echo Notice: Running this script will download and install the necessary python packages needed for the program to run (Pandas, GeoPandas, Plotly)
choice /m "Continue?"
if errorlevel 2 goto end
echo Installing Pandas
python -m pip install pandas

echo Installing GeoPandas
python -m pip install geopandas

echo Installing Plotly
python -m pip install plotly

:end
echo All finished. Exiting.
pause