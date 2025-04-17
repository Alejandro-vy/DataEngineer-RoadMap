SELECT COUNT(ano_creacion) AS cantidad, ano_creacion FROM marcas GROUP BY ano_creacion ORDER BY ano_creacion ASC;


# Lo que hace la sentencia Grioup By es agrupar los resultados de una consulta en función de una o más columnas.

# En este caso, se está agrupando por el año de creación de las marcas y contando cuántas marcas hay en cada año.