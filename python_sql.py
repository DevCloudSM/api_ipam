import psycopg2 as ps

identifiants = {'database':'ipam',
                'user':'postgres',
                'password':'bonjour',
                'host':'localhost',
                'port':5432}

def get_old(tables:list[str], identifiants:dict[str, str]=identifiants) -> list[tuple]:
    with ps.connect(**identifiants) as connector:
        with connector.cursor() as cursor:
            if len(tables) == 1:
                cursor.execute(f"""
                               select * from public."{tables[0]}"
                                """)
            elif len(tables) == 2:
                cursor.execute(f"""
                               select * from public."{tables[0]}"
                               inner join public."{tables[1]}" on public."{tables[0]}".{tables[1]}_id = public."{tables[1]}".id
                               """)
            else:
                return [("Erreur")]
            return cursor.fetchall()

def get(tables:list[str], variable:str="", valeur:str="", identifiants:dict[str, str]=identifiants) -> list[tuple]:
    with ps.connect(**identifiants) as connector:
        with connector.cursor() as cursor:
            if len(tables) >= 3:
                return [('Erreur')]
            commande = f'select * from public."{tables[0]}"'
            if len(tables) == 2:
                commande += f' inner join public."{tables[1]}" on public."{tables[0]}".{tables[1]}_id = public."{tables[1]}".id'
            if variable:
                commande+= f" where {variable} = '{valeur}'"
            cursor.execute(commande)
            return cursor.fetchall()

def put(table:str, data:dict[str,str], identifiants:dict[str, str]=identifiants) -> bool:
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

def delete(table:str, id:int, identifiants:dict[str, str]=identifiants) -> bool:
    try:
        with ps.connect(**identifiants) as connector:
            with connector.cursor() as cursor:
                cursor.execute(f"""
                                delete from public."IP_address" where id = {id}
                                """)
                connector.commit()
                return cursor.rowcount > 0
    except:
        return False

if __name__ == '__main__':
    """User guide de la librairie"""
    print(get(["IP_address"]))
    print(get(["group"], 'name', 'Vannes'))
    print(put(table="IP_address", data={'id':6, 'address': "10.4.2.1"}))
    print(delete("IP_address", 6))
    print(put("subnet", {'id':5, 'first@':'10.0.0.2', 'gp_id':1}))
    print(put("group", {'id':1, 'name':'Vannes'}))