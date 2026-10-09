class Number_analyzer:
  def __init__(self,num):
    self.num = num
  def number_checker(self):
    if  self.num  >  0 :
      print("Number is Postive")
    elif self.num  < 0 :
      print("Number  is  negtive")
    else :
      print ("Number is : 0")

  def even_odd_checker(self):
    if  self.num % 2 == 0 :
      print("Even")
    else :
      print('odd')
  def divider(self):
    if  self.num %  3 == 0 and self.num % 5 == 0 :
      print("Divided  by both 3  and 5  ")
    elif  self.num %  3 == 0 :
      print("divided by  3 only")
    elif self.num % 5 == 0 :
       print("divided by  5")
    else :
             print("Not  divided  by  both")
  def total_value(self):
      total = 0
      temp = self.num
      while temp > 0 :
          last_digit = temp % 10
          total+=last_digit
          temp//=10
      print(f"Total : {total}") 
  def length_digit(self):
        temp = self.num
        count = 0
        while temp > 0 :
            count+=1
            temp//=10
        print(f"Total length :{count}")
  def reverse_num(self):
        reverse_it = 0
        temp = self.num

        while temp > 0:
            last_digit = temp % 10
            reverse_it = (reverse_it * 10) + last_digit
            temp //= 10

        print("Reversed number:", reverse_it)
number_analyizer = Number_analyzer(534353)
number_analyizer.even_odd_checker()
number_analyizer.divider()
number_analyizer.length_digit()
number_analyizer.reverse_num()
number_analyizer.total_value()
