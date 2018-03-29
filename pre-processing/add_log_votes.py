from pymongo import MongoClient

import math

db = MongoClient().imdbws

i = 0
for m in db.movies.find({'log_votes': {'$exists': False}}):
        i += 1
        db.movies.update({'_id': m['_id']},
                         {'$set': {'log_votes':  math.log(m['numVotes'])}})
        if i % 1000 == 0:
            print("{} movies updated.".format(i))