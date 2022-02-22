import re

p = re.compile('ca.e')


# . : 하나의문자를 의미 ca.e -> care, cafe,case,caffe(x)
# ^ : 문자열의 시작 ^de -> desk, destination
# $ : 문자열의 끝 $se -> nise, case


def print_match(model):
    if model:
        print(model.group())
    else:
        print('매칭되지 않음')


print_match(model=p.search('cares'))
print(p.findall('good care cafe'))
# print_match(model=p.match('casse'))


"""
compile (찾고자하는 형태)
match(어떻게 비교해서 찾을건가)
search(소스가 있기만하면 다찾음)
findall(리스트로 긁어올 수 있음)
"""