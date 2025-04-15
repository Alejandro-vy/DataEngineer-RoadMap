SELECT * FROM marcas WHERE NOT ano_creacion = 2015; # Trae todas las columnas de la tabla marcas
                                                    # donde el año de creación no es 2015 

SELECT * FROM marcas WHERE ano_creacion > 2020 AND venta_presencial = 1 # Trae todas las columnas de la tabla marcas
                                                                        # donde el año de creación es mayor a 2020 y la venta presencial es 1                    



SELECT * FROM marcas WHERE ano_creacion > 2020 OR venta_presencial = 1 # Trae todas las columnas de la tabla marcas
                                                                       # donde el año de creación es mayor a 2020 o la venta presencial es 1
