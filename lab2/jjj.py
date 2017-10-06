import GetId
import GetFriendsAges
id = 'lisapol'
ug = 'users.get'
fg = 'friends.get'
idd = GetId.getid()
idf = GetFriendsAges.getfr()
userid = idd._get_data(method=ug, http_method=1)
idf._get_data(method=fg, http_method=1)




