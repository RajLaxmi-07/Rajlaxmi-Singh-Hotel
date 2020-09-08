import random 
import datetime 

# Global List Declaration 
name = [] 
phoneno = [] 
address = [] 
checkindate = [] 
checkoutdate = [] 
room = [] 
rate = [] 
rc = [] 
p = [] 
roomno = [] 
custid = [] 
dayofstay = [] 

# Global Vaariable Declaration 

i = 0

# Home Function 
def Home(): 

	
	print("\t\t WELCOME TO RAJLAXMI HOTEL\n") 
	print("\t\t\t 1 Booking\n") 
	print("\t\t\t 2 Rooms Info\n") 
	print("\t\t\t 3 Room Service(Menu Card)\n") 
	print("\t\t\t 4 Payment\n") 
	print("\t\t\t 5 Record\n") 
	print("\t\t\t 0 Exit\n") 

	ch=int(input("->")) 
	
	if ch == 1: 
		print(" ") 
		Booking() 
	
	elif ch == 2: 
		print(" ") 
		Rooms_Info()  
	
	elif ch == 3: 
		print(" ") 
		Payment()
	
	else: 
		exit() 

# Function used in booking 

def date(c): 
	
	if c[2] >= 2020 and c[2] <= 2021: 
		
		if c[1] != 0 and c[1] <= 12: 
			
			if c[1] == 2 and c[0] != 0 and c[0] <= 31: 
				
				if c[2]%4 == 0 and c[0] <= 29: 
					pass
				
				elif c[0]<29: 
					pass
				
				else: 
					print("Invalid date\n") 
					name.pop(i) 
					phoneno.pop(i) 
					address.pop(i) 
					checkindate.pop(i) 
					checkoutdate.pop(i) 
					Booking() 
			
			
			# if month is odd & less than equal 
			# to 7th month 
			elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31: 
				pass
			
			# if month is even & less than equal to 7th 
			# month and not 2nd month 
			elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2: 
				pass
			
			# if month is even & greater than equal 
			# to 8th month 
			elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31: 
				pass
			
			# if month is odd & greater than equal 
			# to 8th month 
			elif c[1]>=8 and c[1]%2!=0 and c[0]<=30: 
				pass
			
			else: 
				print("Invalid date\n") 
				name.pop(i) 
				phoneno.pop(i) 
				address.pop(i) 
				checkindate.pop(i) 
				checkoutdate.pop(i) 
				Booking() 
				
		else: 
			print("Invalid date\n") 
			name.pop(i) 
			phoneno.pop(i) 
			address.pop(i) 
			checkindate.pop(i) 
			checkoutdate.pop(i) 
			Booking() 
			
	else: 
		print("Invalid date\n") 
		name.pop(i) 
		phoneno.pop(i) 
		address.pop(i) 
		checkindate.pop(i) 
		checkoutdate.pop(i) 
		Booking() 


# Booking fucntion 
def Booking(): 
	
		# used global keyword to 
		# use global variable 'i' 
		global i 
		print(" BOOKING ROOMS") 
		print(" ") 
		
		while 1: 
			n = str(input("Name: ")) 
			p1 = str(input("Phone No.: ")) 
			a = str(input("Address: ")) 
			
			# checks if any field is not empty 
			if n!="" and p1!="" and a!="": 
				name.append(n) 
				address.append(a) 
				break
				
			else: 
				print("\tName, Phone no. & Address cannot be empty..!!") 
			
		cii=str(input("Check-In: ")) 
		checkindate.append(cii) 
		cii=cii.split('/') 
		ci=cii 
		ci[0]=int(ci[0]) 
		ci[1]=int(ci[1]) 
		ci[2]=int(ci[2]) 
		date(ci) 
		
		coo=str(input("Check-Out: ")) 
		checkoutdate.append(coo) 
		coo=coo.split('/') 
		co=coo 
		co[0]=int(co[0]) 
		co[1]=int(co[1]) 
		co[2]=int(co[2]) 
		
		# checks if check-out date falls after 
		# check-in date 
		if co[1]<ci[1] and co[2]<ci[2]: 
			
			print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
			name.pop(i) 
			address.pop(i) 
			checkindate.pop(i) 
			checkoutdate.pop(i) 
			Booking() 
		elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]: 
			
			print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
			name.pop(i) 
			address.pop(i) 
			checkindate.pop(i) 
			checkoutdate.pop(i) 
			Booking() 
		else: 
			pass
		
		date(co) 
		d1 = datetime.datetime(ci[2],ci[1],ci[0]) 
		d2 = datetime.datetime(co[2],co[1],co[0]) 
		d = (d2-d1).dayofstay
		dayofstay.append(d) 
		
		print("----SELECT ROOM TYPE----") 
		print(" 1. Single Bed") 
		print(" 2. Double Bed") 
		print(" 3. Duluxe") 
		 
		print(("\t\tPress 0 for Room Prices")) 
		
		ch=int(input("->")) 
		
		# if-conditions to display alloted room 
		# type and it's price 
		if ch==0: 
			print(" 1. Single Bed - Rs. 1500") 
			print(" 2. Double Bed - Rs. 3000") 
			print(" 3. Duluxe - Rs. 5000") 
			 
			ch=int(input("->")) 
		if ch==1: 
			room.append('Single Bed') 
			print("Single Bed") 
			price.append(1500) 
			print("Price- 1500") 
		elif ch==2: 
			room.append('Double Bed') 
			print("Double Bed") 
			price.append(3000) 
			print("Price- 3000") 
		elif ch==3: 
			room.append('Duluxe') 
			print("Duluxe") 
			price.append(5000) 
			print("Price- 5000") 
		
		else: 
			print(" Wrong choice..!!") 


		# randomly generating room no. and customer 
		# id for customer 
		rn = random.randrange(40)+300
		cid = random.randrange(40)+10
		
		
		# checks if alloted room no. & customer 
		# id already not alloted 
		while rn in roomno or cid in custid: 
			rn = random.randrange(60)+300
			cid = random.randrange(60)+10
			
		rc.append(0) 
		p.append(0) 
				
		if p1 not in phoneno: 
			phoneno.append(p1) 
		elif p1 in phoneno: 
			for n in range(0,i): 
				if p1== phoneno[n]: 
					if p[n]==1: 
						phoneno.append(p1) 
		elif p1 in phoneno: 
			for n in range(0,i): 
				if p1== phoneno[n]: 
					if p[n]==0: 
						print("\tPhone no. already exists and payment yet not done..!!") 
						name.pop(i) 
						address.pop(i) 
						checkindate.pop(i) 
						checkoutdate.pop(i) 
						Booking() 
		print("") 
		print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n") 
		print("Room No. - ",rn) 
		print("Customer Id - ",cid) 
		roomno.append(rn) 
		custid.append(cid) 
		i=i+1
		n=int(input("0-BACK\n ->")) 
		if n==0: 
			Home() 
		else: 
			exit() 

# ROOMS INFO 
def Rooms_Info(): 
	print("		 ------ HOTEL ROOMS INFO ------") 
	print("") 
	print(" Single Bed") 
	print("---------------------------------------------------------------") 
	print("Room facilities include: Breakfast, AC, Intercom,") 
	print("Laundry, Canteen Service") 
	print("Double Bed") 
	print("---------------------------------------------------------------") 
	print("Room facilities include: Breakfast, AC, Intercom,") 
	print("Laundry, Canteen Service, Double Cot, Blanket, Sofa Set, a Shelf") 
	print("Dulexe ") 
	print("---------------------------------------------------------------") 
	print("Room facilities include: Breakfast, AC, Intercom,") 
	print("Laundry, Canteen Service, Double Cot, Blanket,") 
	print("Sofa Set, 2 Shelf, Fridge, a microoven ") 
	 
	print() 
	n=int(input("0-BACK\n ->")) 
	if n==0: 
		Home() 
	else: 
		exit() 

				
# PAYMENT FUNCTION			 
def Payment(): 
	
	ph=str(input("Phone Number: ")) 
	global i 
	f=0
	
	for n in range(0,i): 
		if ph==phoneno[n] : 
			
			# checks if payment is 
			# already done 
			if p[n]==0: 
				f=1
				print(" Payment") 
				print(" --------------------------------") 
				print(" MODE OF PAYMENT") 
				
				print(" 1- Credit/Debit Card") 
				print(" 2- Paytm/PhonePe") 
				print(" 3- Using UPI") 
				print(" 4- Cash") 
				x=int(input("-> ")) 
				print("\n Amount: ",(price[n]*dayofstay[n])+rc[n]) 
				print("\n		 Pay For Rajlaxmi Hotel") 
				print(" (y/n)") 
				ch=str(input("->")) 
				
				if ch=='y' or ch=='Y': 
					print("\n\n --------------------------------") 
					print("		 Rajlaxmi Hotel") 
					print(" --------------------------------") 
					print("			 Bill") 
					print(" --------------------------------")
					print(" Single Room Rate- 1500")
					print(" Double Room Rate- 300")
					print(" Duluxe Room Rate- 5000")

					print(" Name: ",name[n],"\t\n Phone No.: ",phoneno[n],"\t\n Address: ",address[n],"\t") 
					print("\n Check-In: ",checkindate[n],"\t\n Check-Out: ",checkoutdate[n],"\t") 
					print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*dayofstay[n],"\t") 
					 
					print(" --------------------------------") 
					print("\n Total Amount: ",(price[n]*dayofstay[n])+rc[n],"\t") 
					print(" --------------------------------") 
					print("		 Thank You so much") 
					print("		 Visit Again :)") 
					print(" --------------------------------\n") 
					p.pop(n) 
					p.insert(n,1) 
					
					# pops room no. and customer id from list and 
					# later assigns zero at same position 
					roomno.pop(n) 
					custid.pop(n) 
					roomno.insert(n,0) 
					custid.insert(n,0) 
					
			else: 
				
				for j in range(n+1,i): 
					if ph==phoneno[j] : 
						if p[j]==0: 
							pass
						
						else: 
							f=1
							print("\n\tPayment has been Made :)\n\n") 
	if f==0:	 
		print("Paid Successfully") 
		
	n = int(input("0-BACK\n ->")) 
	if n == 0: 
		Home() 
	else: 
		exit() 


# Driver Code 
Home() 
