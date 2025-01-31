import requests
import pprint

URL = 'https://fakestoreapi.com/carts'  # 문자열을 가져오는 등의 하드코딩을 할 때는 변수명을 대문자로 설정하는 편.
data = requests.get(URL)  # requests의 get method로 URL의 데이터를를 가져옴.
# [200]. 웹의 응답 코드. == 정상적으로 응답함.
# [404]: not found. 알 수 없는 주소로 요청함. 아주 유명하쥬?  # 404가 뜬다면, URL 오타를 점검할 것.
# '상태 코드'로 찾아보면 많이 나올 듯.
print(data)

json_data = data.json()  # requests의 get method로 가져온 URL 데이터를 json method로 받아들일 수 있게 가공.
print(json_data)
pprint.pprint(json_data)  # from pprint import pprint로 pprint 내의 pprint method를 가져와서 pprint만 하는 방법도 있음.