import json
from pprint import pprint
from copy import deepcopy

def artist_info(artist, genres):

    new_lst = []
    my_dict = {}
    return_lst = []

    for el_dict in artist:
        my_dict.update(el_dict)
        my_dict.pop('external_urls')
        my_dict.pop('uri')

        for num in range(len(my_dict['genres_ids'])):  # my_dict의 genres_ids의 value의 길이만큼 반복하는데~
            for el in genres:  # genres_list의 모든 요소에 대해~
                if el['id'] == my_dict['genres_ids'][num]:  # genres_list의 ids의 value가 my_dict의 genres_ids의 요소와 같다면~ 
                    my_dict['genres_ids'][num]= el['name']  # my_dict의 genres_ids의 value 값을 genres명으로 바꾼다

        new_lst.append(my_dict)  # new_lst에 my_dict 딕셔너리를 넣고
        copy_lst = deepcopy(new_lst)  # new_lst를 deepcopy.
        return_lst.append(copy_lst)  # deepcopy한 값을 새로운 list에 정리.

        my_dict.clear()  # 초기화
        new_lst = []  # 초기화

    return return_lst

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':  # 이 파일에 대해~
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent  # 이 파일의 상위 폴더 경로를 절대경로로 current_dir에 넣는다.

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')  # 경로를 따라 artists.json파일을 연다.
    artists_list = json.load(artist_json)  # json파일을 해석할 수 있는 형태로 가공한다.

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')  # 경로를 따라 genres.json파일을 연다.
    genres_list = json.load(genres_json)  # json파일을 해석할 수 있는 형태로 가공한다.

    pprint(artist_info(artists_list, genres_list))  # 두 json파일을 이용해 함수를 적용한다.
