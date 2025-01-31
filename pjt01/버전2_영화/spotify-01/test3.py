import json
from pprint import pprint
from copy import deepcopy


# import json
# from pprint import pprint
# from copy import deepcopy


# def artist_info(artist):
    
#     new_lst = []

#     for el in artist:
#         new_lst.append(el['id'])

#     return new_lst


# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     from pathlib import Path

#     current_dir = Path(__file__).resolve().parent

#     artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
#     artists_list = json.load(artist_json)

#     print(artist_info(artists_list))



# def artist_info(artist, genres):

#     new_lst = []
#     my_dict = {}
#     return_lst = []

#     for el_dict in artist:
#         my_dict.update(el_dict)  # update를 사용하면 사용하지 않는 'external_urls', 'uri'도 들어온다.
#         my_dict.pop('external_urls')
#         my_dict.pop('uri')  # 그러니까, external_urls와 uri를 pop해서 쓰면 된다.

#         for num in range(len(my_dict['genres_ids'])):
#             for el in genres:
#                 if el['id'] == my_dict['genres_ids'][num]:
#                     my_dict['genres_ids'][num]= el['name']

#         new_lst.append(my_dict)
#         copy_lst = deepcopy(new_lst)
#         return_lst.append(copy_lst)

#         my_dict.clear()
#         new_lst = []

#     return return_lst






def artist_info(artist):

    my_dict = {}
    my_dict.update(artist) 

    return my_dict['popularity']

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists' / '116.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))