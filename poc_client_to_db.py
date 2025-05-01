from asyncua import Client
import psycopg2
import asyncio

async def fetch_and_store():
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    await client.connect()
    conn = psycopg2.connect("dbname=sensors user=user password=pass host=localhost port=55432")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            time TIMESTAMPTZ DEFAULT now(),
            temperature FLOAT,
            pressure FLOAT
        );
    """)
    conn.commit()

    try:
        obj = await client.nodes.root.get_child(["0:Objects", "2:SensorBox"])
        temp = await obj.get_child("2:Temperature")
        pressure = await obj.get_child("2:Pressure")

        while True:
            t_val = await temp.read_value()
            p_val = await pressure.read_value()
            cur.execute("INSERT INTO sensor_data (temperature, pressure) VALUES (%s, %s);", (t_val, p_val))
            conn.commit()
            print(f"Logged: Temp={t_val}, Pressure={p_val}")
            await asyncio.sleep(2)
    finally:
        await client.disconnect()
        cur.close()
        conn.close()

asyncio.run(fetch_and_store())
