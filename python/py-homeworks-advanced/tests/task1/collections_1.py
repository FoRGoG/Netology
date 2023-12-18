def ids_func():
       ids = {'user1': [213, 213, 213, 15, 213],
              'user2': [54, 54, 119, 119, 119],
              'user3': [213, 98, 98, 35]}

       ids_set1 = set(ids['user1'])
       ids_set2 = set(ids['user2'])
       ids_set3 = set(ids['user3'])
       result = ids_set1 | ids_set2 | ids_set3
       return result

