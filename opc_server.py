from asyncua import Server
import asyncio
import random

async def main():
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    namespace = await server.register_namespace("IndustrialSensors")
    obj = await server.nodes.objects.add_object(namespace, "SensorBox")

    temp = await obj.add_variable(namespace, "Temperature", 20.0)
    pressure = await obj.add_variable(namespace, "Pressure", 1.0)

    await temp.set_writable()
    await pressure.set_writable()

    async with server:
        print("OPC UA Server running at opc.tcp://0.0.0.0:4840/freeopcua/server/")
        while True:
            await temp.write_value(random.uniform(15.0, 35.0))
            await pressure.write_value(random.uniform(0.8, 1.2))
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
