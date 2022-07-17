# bounce.py
#
# Exercise 1.5
def bounce(height,num_bounces):
	print("You are bouncing a ball from", height," meters high,",num_bounces, " times")
	while num_bounces > 0:
		height  *= .6
		print("Bounce Height:", round(height,4))
		num_bounces -= 1

bounce(100,10)
