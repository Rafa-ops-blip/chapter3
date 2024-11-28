#friends list
friend = ['faridah', 'grace','halimah','favour']
print(friend[0].title())
print(friend[1].title())
print(friend[2].title())
print(friend[3].title())
message_1 = f"{friend[0].title()} is my friend"
print(message_1)
message_2 = f"{friend[1].title()} is my friend"
print(message_2)
message_3 = f"{friend[2].title()} is my friend"
print(message_3)
message_4 = f"{friend[3].title()} is my friend"
print(message_4)

#list of cars
cars = ['Mazda', 'mercedes', 'toyota', 'ferrari', 'volskwagen']
message = f"I'd like to own a {cars[3].title()} that looks like a {cars[0]} and has a {cars[1].title()} engine"
print(message)

#Guest list
guests = ['Hannat', 'Bushrah', 'Hauwa']

message = f"""I would like to invite you Miss {guests[0]} to my birthday dinner 
coming up on the first day of the month of December."""
print(message)

message = f"""I would like to invite you Miss {guests[-1]} to my birthday dinner 
coming up on the first day of the month of December."""
print(message)

message = f"""I would like to invite you Miss {guests[1]} to my birthday dinner 
coming up on the first day of the month of December."""
print(message)

guests[0] = 'Aliyah'
message = f"""I would like to invite you Miss {guests[0]} to my birthday dinner coming up on the first day of the month of December."""
print(message)

print(guests)

#Add three more guests
guests.insert(0, 'Aishah')
guests.insert(2, 'fareedah')
guests.append('salmah')

print(guests)

message = f"I'm so sorry for the inconveniences. There has been a change of plans. Due to some unforseen circumstances, i can only invite two people for my birthday dinner. "
print(message)

#Remove some guests from the list
popped_guest = guests.pop(0)
message = f"I'm sorry {popped_guest}, youre not invited to my birthday dinner."
print(message)

popped_guest = guests.pop(-1)
message = f"{popped_guest.title()} you have a bad character, you're not invited."
print(message)

popped_guest = guests.pop(3)
message = f"{popped_guest} you have a bad character, you're not invited."
print(message)

popped_guest = guests.pop(1)
message = f"I'm sorry {popped_guest.title()}, you're not invited to my birthday dinner."
print(message)

print(guests)
message = f"Dear {guests[0]},\nYou're still invited to my birthday dinner\nYours Truely"
print(message)
message = f"Dear {guests[1]},\nYou're still invited to my birthday dinner\nYours Truely"
print(message)

del guests[0]
print(guests)

del guests[0]
print(guests)

#places to visit
place = ['Saudi', 'United Kingdom', 'Finland', 'India', 'Maldives', 'Canada']
print(place)
print(sorted(place))
print(place)

place.reverse()
print(place)

place.reverse()
print(place)

place.sort()
print(place)

place.sort(reverse=True)
print(place)

#dinner guests
guests = ['Hannat', 'Bushrah', 'Hauwa']
len(guests)
print(guests)
len(guests)
message = f'we have {len(guests)} guests'
print(message)
print(guests[-1])