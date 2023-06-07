#!/bin/bash

echo "MySQL is unavailable - sleeping"
sleep 10

echo "MySQL is up - executing command"
echo $DATABASE_URL
if [ "${DATABASE_URL}" = "mysql://user:password@db/TURTLE_BEE" ]; then
    echo "Modo de Desenvolvimento Ativado"
    
    prisma generate
    prisma format
    prisma db push
    python app.py
else
    echo "Modo de Desenvolvimento Desativado"

    prisma generate
    prisma format
    python app.py
    
fi