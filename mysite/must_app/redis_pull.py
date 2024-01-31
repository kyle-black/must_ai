import redis


def data_pull():
    r = redis.Redis(
    host='redis-17905.c326.us-east-1-3.ec2.cloud.redislabs.com',
    port=17905,
    password='zHeoOL4uqpzaxTC7YgtuWvq4HRNSsoD0')

    AUDUSD = r.xrange("security:AUDUSD")

    AUDUSD_dict ={}

    for i in AUDUSD:
      unix = int(i[0].decode('utf-8').replace('-0', ''))
      data = {k.decode('utf-8'): v.decode('utf-8') for k, v in i[1].items()}
      AUDUSD_dict[unix] = data

    #print(AUDUSD_dict)
        
      

    

    return AUDUSD_dict


#print(redis_pull())
