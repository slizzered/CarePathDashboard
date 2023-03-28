async def cursor_to_json(cursor):
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return await table_to_json(rows, columns)


async def table_to_json(rows, columns):
    return [await row_to_dict(row, columns) for row in rows]


async def row_to_dict(row, columns):
    return {col: row[i] for i, col in enumerate(columns)}
