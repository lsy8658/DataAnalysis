# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# # 첫 두 행 출력


# print(matrix[0], matrix[1])

# # 첫 두 열 출력

# print(matrix[0:2])

#==============================================

# numbers = []
# for i in range(5):
#     print(i)
# print('numbers => ', numbers)

#==============================================
# 딕셔너리 => 객체라 보면됨 키와 값으로 이루어진 쌍의 집합

# city_population = {
#     '서울': 957, '부산': 339, '인천': 294, '대구': 242, '광주': 145, '대전': 147,
#     '울산': 114, '세종': 36, '수원': 115, '창원': 103, '고양': 105, '용인': 108, '성남': 94
# }

# 인구 300만 이상 및 이름에 '산'이 포함된 도시 리스트

# large_short_name_cities = []
# for i in city_population:
#     if '산' in i :
#         large_short_name_cities.append(city_population[i])
# print(large_short_name_cities)