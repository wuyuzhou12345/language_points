import redis
r = redis.Redis(host="127.0.0.1",port=6379)

#string类型的相关操作 set既可以没有相关的值然后开始设置也可以是进行update操作 get获取  del删除
r.set('hello2021', 'world2025')
print(r.get('hello2021'))
r.delete('hello2021')
print(r.get('hello2021'))

#zset相关类型的操作 sorted set  zadd zrange zrevrange
r.zadd("userid:201345",{"english":1,"chinese":2})
print(r.zrange("userid:201345",0,-1))
r.zrem("userid:201345","english")
print(r.zrange("userid:201345",0,-1))

#hash相关类型的操作 hget hgetall hset hmset del
print(r.hget("hash_user:zhouluying","age"))
print(r.hgetall("hash_user:zhouluying"))
r.hset("hash_user:zhouluying","name","zly")
# r.hmset("hash_user:zly",{"name":"zly","age":18,"no":3})
print(r.hgetall("hash_user:zly"))
r.delete("hash_user:zhouluying")
print(r.hgetall("hash_user:zly"))

#list相关类型的操作 lpush rpush
r.lpush("list_user:201345","[1,2,3,4,5]")
print(r.lrange("list_user:201345",0,-1))
r.lpop("list_user:201345")
print(r.lrange("list_user:201345",0,-1))

#set相关类型的操作 sadd smemebers del
r.sadd("set:201345","english","chinese")
print(r.smembers("set:201345"))
r.delete("set:201345")
print(r.smembers("set:201345"))