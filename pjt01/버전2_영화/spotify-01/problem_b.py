import json
from pprint import pprint

def artist_info(artist, genres):

    my_dict = {}
    my_dict.update(artist)
    my_dict.pop('external_urls')
    my_dict.pop('uri')

    for num in range(len(my_dict['genres_ids'])):  # my_dict의 genres_ids의 value 길이만큼 반복하는데~
        for el in genres:  # genres_list의 모든 요소에 대해~
            if el['id'] == my_dict['genres_ids'][num]:  # genres_list의 ids의 value가 my_dict의 genres_ids의 요소와 같다면~
                 my_dict['genres_ids'][num]= el['name']  # my_dict의 genres_ids의 value 값을 genres명으로 바꾼다

    return my_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':  # 이 파일에 대해~
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent  # 이 파일의 상위 폴더 경로를 절대경로로 current_dir에 넣는다.

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')  # 경로를 따라 artist.json파일을 연다.
    artist_dict = json.load(artist_json)  # json파일을 해석할 수 있는 형태로 가공한다.

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')  # 경로를 따라 genres.json파일을 연다.
    genres_list = json.load(genres_json)  # json파일을 해석할 수 있는 형태로 가공한다.

    pprint(artist_info(artist_dict, genres_list))  # 두 json파일을 이용해 함수를 적용한다.
