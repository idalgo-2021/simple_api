import sqlite3 as sq

# Параметры базы данных
DATABASE = 'database.db'
SCHEME = 'schem.sql'


# Подключение базы данных
def connect_db():
    return sq.connect(DATABASE)


# Создание базы данных (по скрипту из SCHEME)
def create_db():
    connection = connect_db()
    cursor = connection.cursor()
    with open(SCHEME, mode='r') as file:
        scheme_script = file.read()
    cursor.executescript(scheme_script)
    connection.commit()
    cursor.close()
    connection.close()


# Вспомогательная функция для упрощения получения результатов по ключу
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def select_items(item_id=None):
    my_list = []
    connection = connect_db()

    if item_id == None:
        sql = "SELECT * FROM items"
    else:
        sql = f"SELECT * FROM items WHERE id = {item_id}"

    try:
        cursor = connection.execute(sql)
        cursor.row_factory = dict_factory
        for row in cursor:
            record = {
                'name': row.get('name'),
                'id': row.get('id'),
                'folder_id': row.get('folder_id'),
                'is_weighted': row.get('is_weighted'),
                'description': row.get('description'),
            }
            my_list.append(record)

    except connection.Error as error:
        print("Error connection to database", error)
    finally:
        if connection: connection.close()

    return my_list


# Заполнение тестовыми данными
items = [
    (1, 'Вентилятор BINATONE ALPINE 160вт, напольный ,', 1, 0, 'Вентилятор BINATONE ALPINE 160вт, напольный , оконный'),
    (2, 'Вентилятор JIPONIC (Тайв.),', 1, 0, 'Вентилятор JIPONIC (Тайв.), напольный'),
    (3, 'Вентилятор настольный', 1, 0, 'Вентилятор настольный'),
    (4, 'Вентилятор ОРБИТА,STERLING,ЯП.', 1, 0, 'Вентилятор ОРБИТА,STERLING,ЯП.'),
    (5, 'Пылесос "Омега" 1250вт', 1, 0, 'Пылесос "Омега" 1250вт'),
    (6, 'Телевизор "SHARP"', 3, 0, 'Телевизор "SHARP"'),
    (7, 'Набор кухонной мебели (цвет белый)', 4, 0, 'Набор кухонной мебели (цвет белый)'),
]


def insert_testdata():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO items VALUES(?, ?, ?, ?, ?)", items)
    connection.commit()
    connection.close()


def test2():
    print(select_items(2))
