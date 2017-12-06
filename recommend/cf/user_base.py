‘’‘
read data from file(ratings.csv, [userId,movieId,rating,timestamp])
build up the map: {uid: {movieId:rating}}
also build the map: {moveId: [uid1, uid2]}

change the {uid:{moverId:rating}} to the matrix/vector
should consider how unexisting item is scored

core of user-based cf
calculate the sim between different users
filter the users whose sim is larger than some value we set
use those filtered users to predict the score for the movie
sort the list
’‘’