#01 Example
friends = ["Rolf", "Sam", "Samantha", "Saurabh"]

#Another Example
starts_s = [friend for friend in friends if friend.startswith("S")]

#Second Example(Another Method Of The Previous One/(Repeats))
for friend in friends:
	if friend.startswith("S"):
		starts_s.append(friend)

print(friends)
print(starts_s)
print(friends[0] is starts_s[0])
print("friends: ",id(friends), "starts_s:", id(starts_s))