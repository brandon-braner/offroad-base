import motor.motor_asyncio

uri = "mongodb://root:password@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(uri)