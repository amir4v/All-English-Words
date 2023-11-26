from PriorityRandom import PR


A1 = open('A1', 'rt', encoding='utf-8').read().split('\n')
A2 = open('A2', 'rt', encoding='utf-8').read().split('\n')
B1 = open('B1', 'rt', encoding='utf-8').read().split('\n')
B2 = open('B2', 'rt', encoding='utf-8').read().split('\n')
C1 = open('C1', 'rt', encoding='utf-8').read().split('\n')
C2 = open('C2', 'rt', encoding='utf-8').read().split('\n')

ALL = [
    A1, A2,
    B1, B2,
    C1, C2
]

COMBINED = []

for i in range(1, len(ALL)+1):
    for level in ALL:
        for word in level:
            COMBINED.append((word, i))

pr = PR(COMBINED)

print(pr.choices(10))
