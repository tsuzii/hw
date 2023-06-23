import random

members = [
    'Кирилл',
    'Лилия',
    'Александр',
    'Сергей',
    'Андрей',
    'Резеда',
    'Дмитрий',
    'Миша',
    'Полина',
]

random.shuffle(members)

groups = []
for i in range(0, len(members), 2):
    group = members[i:i+2]
    if len(group) == 1:
        groups[-1].extend(group)
    else:
        groups.append(group)

reviewers_count = len(groups)
reviewers = [group[-1] for group in groups]

while True:
    random.shuffle(reviewers)
    groups_with_review = list(zip(groups, reviewers))
    for group, reviewer in groups_with_review:
        if reviewer in group:
            break
    else:
        break

for no, (group, reviewer) in enumerate(groups_with_review, 1):
    print('Группа {}\\'.format(no))
    print('Лид: {}\\'.format(group[0]))
    print('Про: {}\\'.format(', '.join(group[1:])))
    print('Ревью: {}'.format(reviewer))
    print()
