#Credits to Austin Daly

import heapq

#Gets minimum of function
def minimum(a, b, c):
	m = 0

	#Gets smaller of two
	if a > b:
		m = b
	else:
		m = a

	#Checks c with smaller of two
	if m > c:
		return c
	else:
		return m

#Gets distance between two strings
def levingsteinDistance(s1, s2):
	s1Size = len(s1)
	s2Size = len(s2)

	a = get2DArray(s1Size+1, s2Size+1)

	#Initializes bottem elements in array
	for i in range(0, s1Size):
		a[0][i+1] = i+1

	for j in range(0, s2Size):
		a[j+1][0] = j+1

	for j in range(0, s2Size):
		for i in range(0, s1Size):

			#Sets up sub cost
			subCost = 1;

			#If the chars in string is the same
			if ( s2[j] == s1[i] ):
				subCost = 0
			#                     Deletion     Insertion     Substitution
			a[j+1][i+1] = minimum(a[j+1][i]+1, a[j][i+1] +1, a[j][i] + subCost)

	return a[s2Size][s1Size]

#Generates 2d array
def get2DArray(width, height):
	arr = [0]*height
	for i in range(0, height):
		arr[i] = [0]*width
	return arr

#Search Algorithm
def search(query, workouts):
	h = []

	#Loops through the list
	for workout in workouts:
		heapq.heappush(h, (workoutVal(query, workout), workout))

	return [heapq.heappop(h)[1] for i in range(len(h))]
	#return order from closest to farthest

def workoutVal(s, work):
	return 0.9*workoutSearch(s, work, 0)+0.075*workoutSearch(s, work, 1)+0.025*workoutSearch(s, work, 2)

def workoutSearch(s, work, itm):
	val = -1

	if itm == 0:
		val = levingsteinDistance(s, work.title)
	else:
		if itm == 1:
			val = levingsteinDistance(s, work.description)
		else:
			val = levingsteinDistance(s, work.notes)

	return val
