import psycopg2 as ps

identifiants = {'database':'ipam',
                'user':'postgres',
                'password':'bonjour',
                'host':'localhost',
                'port':5432}

def get(identifiants:dict[str, str], table:str) -> list[tuple]:
    with ps.connect(**identifiants) as connector:
        with connector.cursor() as cursor:
            table_2 = ""
            cursor.execute(f"""select * from public."{table}"
                                inner join {table_2}
                           """)
            return cursor.fetchall()

def put(identifiants:dict[str, str], table:str, data:dict[str,str]) -> bool:
    try:
        with ps.connect(**identifiants) as connector:
            with connector.cursor() as cursor:
                cursor.execute(f"""
                    insert into public."{table}" values ({", ".join([f"'{x}'" if type(x) == str else str(x) for x in data.values()])})
                    """)
                connector.commit()
                return True
    except:
        return False

def delete(identifiants:dict[str, str], table:str, id:int) -> bool:
    try:
        with ps.connect(**identifiants) as connector:
            with connector.cursor() as cursor:
                cursor.execute(f"""
                                delete from public."IP_address" where id = {id}
                                """)
                connector.commit()
                return True
    except:
        return False

if __name__ == '__main__':
    """User guide de la librairie"""
    print(get(identifiants, "IP_address"))
    print(put(identifiants, table="IP_address", data={'id':6, 'address': "10.4.2.1"}))
    print(delete(identifiants, "IP_address", 254))