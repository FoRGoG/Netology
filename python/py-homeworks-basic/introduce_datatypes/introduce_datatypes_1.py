boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()

number_of_boys = len(boys)
number_of_girls = len(girls)

zipped_pro = zip (boys, girls)

if number_of_boys == number_of_girls:
  print("Идеальные пары:")
  for boys, girls in zipped_pro:
    print(f"{boys} и {girls}")
else:
  print("Кто-то может остаться без пары!")
