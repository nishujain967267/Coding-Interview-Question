def findLargestSumPair(arr, n): 

 
	if arr[0] > arr[1]: 
		first = arr[0] 
		second = arr[1] 
	
	else: 
		first = arr[1] 
		second = arr[0] 
	
	for i in range(2, n): 
		if arr[i] > first: 
			second = first 
			first = arr[i] 
		elif arr[i] > second and arr[i] != first: 
			second = arr[i] 
	
	return (first * second) 
arr = [2,7,1,3,4,5] 
n = len(arr) 
print("Max Pair product is",findLargestSumPair(arr, n)) 

 
