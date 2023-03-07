from django.shortcuts import render

# Create your views here.
people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
def age1(request):
    func = lambda d: d['age']
    func(people[0])
    people.sort(key = func)

    return render(request,'age1.html',people)

def people1(request, id: int):
    person = None
    for x in people:
        if people['id'] == id:
            person = x
    
    return render(request,'person.html',person)
