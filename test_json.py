'''import json

data = '''
#{"response":{"GeoObjectCollection":{"metaDataProperty":{"GeocoderResponseMetaData":{"request":"аэропорт Внуково","results":"10","found":"2"}},"featureMember":[{"GeoObject":{"metaDataProperty":{"GeocoderMetaData":{"precision":"other","text":"Россия, Москва, аэропорт Внуково имени А.Н. Туполева","kind":"airport","Address":{"country_code":"RU","formatted":"Россия, Москва, аэропорт Внуково имени А.Н. Туполева","Components":[{"kind":"country","name":"Россия"},{"kind":"province","name":"Центральный федеральный округ"},{"kind":"province","name":"Москва"},{"kind":"airport","name":"аэропорт Внуково имени А.Н. Туполева"}]},"AddressDetails":{"Country":{"AddressLine":"Россия, Москва, аэропорт Внуково имени А.Н. Туполева","CountryNameCode":"RU","CountryName":"Россия","AdministrativeArea":{"AdministrativeAreaName":"Москва","Locality":{"DependentLocality":{"DependentLocalityName":"аэропорт Внуково имени А.Н. Туполева"}}}}}}},"name":"аэропорт Внуково имени А.Н. Туполева","description":"Москва, Россия","boundedBy":{"Envelope":{"lowerCorner":"37.229833 55.583169","upperCorner":"37.303809 55.61598"}},"Point":{"pos":"37.286292 55.605058"}}},{"GeoObject":{"metaDataProperty":{"GeocoderMetaData":{"precision":"other","text":"Россия, Киевское направление Московской железной дороги, платформа Аэропорт Внуково","kind":"railway_station","Address":{"country_code":"RU","formatted":"Россия, Киевское направление Московской железной дороги, платформа Аэропорт Внуково","Components":[{"kind":"country","name":"Россия"},{"kind":"province","name":"Центральный федеральный округ"},{"kind":"route","name":"Киевское направление Московской железной дороги"},{"kind":"railway_station","name":"платформа Аэропорт Внуково"}]},"AddressDetails":{"Country":{"AddressLine":"Россия, Киевское направление Московской железной дороги, платформа Аэропорт Внуково","CountryNameCode":"RU","CountryName":"Россия","Country":{"Locality":{}}}}}},"name":"платформа Аэропорт Внуково","description":"Киевское направление Московской железной дороги, Россия","boundedBy":{"Envelope":{"lowerCorner":"37.279914 55.601106","upperCorner":"37.296371 55.610423"}},"Point":{"pos":"37.288142 55.605765"}}}]}}}'''

'''resp = json.loads(data)

print(resp["GeoObjectCollection"]["featureMember"]["GeoObject"]['metaDataProperty']['GeocoderMetaData']['kind'])'''


import json

s = {'Иван': 24, 'Сергей': 11}
print(json.dumps(s, ensure_ascii=False, indent=4))