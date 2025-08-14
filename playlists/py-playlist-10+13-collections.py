from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

device_temp = [12, 14.5, 14.5, 14.5, 13, 13, 13, 13, 11, 12]
c = Counter(device_temp)
print(c[14.5])
print(c[13])

l = defaultdict(list)
coworkers = ['Ram', 'Rani', 'Raj', 'Rahul']
my_company = 'Telcado'
coworker_companies = [('Rahul', 'Apple'), ('Rahul', 'Microsoft'), ('Raj', 'Slack'), ('Rat', 'Salesforce')]

all_coworkers = ['Ram', 'Rani', 'Raj', 'Rahul', 'Rat']

for emp, company in coworker_companies:
    l[emp].append(company)
    
print(l)

d = defaultdict(lambda: [my_company])

for emp in all_coworkers:
    if l.get(emp) is not None:
        d[emp] = l[emp]
    else:
        d[emp]
        
print(d)

od = OrderedDict()
od['Jack'] = 5
od['Jill'] = 12
od['Jim'] = 15
od['Jerry'] = 16

x = od.popitem()
print(x)
print(od)
od.move_to_end('Jack')
od.move_to_end('Jim', last=False)
print(od)

account = ('checking', 1568.50)
Account = namedtuple('Account', ['name', 'balance'])
accountnamedtuple = Account(*account)
acc_namedtuple = Account._make(account)
ac_namedtuple = Account(name='checking', balance=1578.5)
print(accountnamedtuple)
print(acc_namedtuple)
print(ac_namedtuple)

print(acc_namedtuple._asdict)

d = deque([1, 2, 3, 4, 5])
d.appendleft(6)
d.append(7)
print(d)
print(d.pop())
print(d.popleft())