print(46 + 37 + 38)
print((42*60)+42)
print(10/1.61)
print(2562/60)
print(42.7/6.2111)
print(42.7/60)
print(6.211/(42.7/60))


#Earlier, my file was quite clunky, and quite lacking. I apologize for that professor, I didn't 
#realize how we were to format it. Hopefully this time it is better. 

#Question 1
pi = 3.1415
r = 5
Volume = ( 4 / 3) * pi * (r**3)
Volume #Answer


#or
pi = 3.1415
r = 5
print('The volume of a sphere with radius 5 is {}'. format((4/3)*pi*r**3.))

#Question 2
#Suppose the price is 24.95, but bookstore gets 40% discount.
#Shipping is $3 for first copy, and 75 cents for additional ones.
#What is wholesale cost for 60 copies. 

price = 24.95
discount = .4
First_Ship = 3
Add_Ship = .75

print('The cost of the 60 copies is {}'. format((price*(1-discount)*60)+First_Ship+(59*Add_Ship)))

#Question 3
#if I leave my house at 6:52 am and run 1 mile at 8:15 pace
#then 3 miles at 7:12 per mile, and 1 mile at easy pace again
#What time to I get home for breakfast?

T1_in_minutes = 6*60+52
Mile_Easy = 8+(15/60)
Miles_Tempo = 3*(7+(12/60))

print('The time I get home for breakfast is {}'. format((T1_in_minutes+Mile_Easy+Miles_Tempo)/60)) 
#The answer comes out as 7.364166, which when converted back to 

#Question 4
#If avg. grade rises from 82 to 89, what is percentage of increase?
Initial_grade = 82
Final_grade = 89
IG = Initial_grade
FG = Final_grade
Dif = FG-IG

print('The average grade raise, in percentage terms is {}%'. format((Dif/IG)*100))
