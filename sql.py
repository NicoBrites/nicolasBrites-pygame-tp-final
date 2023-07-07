class Sql:
    
    @staticmethod
    def agregar_datos(nombre,puntaje,lvl):
        import sqlite3
        if lvl == 1:
            conexion=sqlite3.connect("JUEGO_ON/db/score_lvl1.db")
        elif lvl == 2:
            conexion=sqlite3.connect("JUEGO_ON/db/score_lvl2.db")
        else:
            conexion=sqlite3.connect("JUEGO_ON/db/score_lvl3.db")
        try:
            conexion.execute("insert into score (nombre,value) values (?,?)", (nombre, puntaje))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")
          
    @staticmethod
    def crear_tabla(lvl):
        import sqlite3
        if lvl == 1:
            conexion=sqlite3.connect("JUEGO_ON/db/score_lvl1.db")
        elif lvl == 2:
            conexion=sqlite3.connect("JUEGO_ON/db/score_lvl2.db")
        else:
            conexion=sqlite3.connect("JUEGO_ON/db/score_lvl3.db")
        try:
            conexion.execute(''' create  table score
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        value real
                                )
                            ''')
            print("se creo la tabla")
        except sqlite3.OperationalError:
            print("La tabla ya existe")
        conexion.close()
