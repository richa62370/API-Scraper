import aioredis

async def get_redis():
    redis = await aioredis.create_redis_pool('redis://localhost')
    return redis
