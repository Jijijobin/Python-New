Name=["Sub-field in AI are:","Machine Learning","Neutral Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
class Variousfield():
    def subfields():
       for data in Name:
          print(data)
  
    def oddeven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is even number")
            out="Even number"
        else:
            print(num,"is odd number")
            out="Odd number"

    def ageeligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age<=20):
            print("Not Eligible")
            out="Not Elligible"
        else:
            print("Eligible")
            out="Eligible"
        return out

    def percentage():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        Total=Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total:",Total)
        per=float(Total)*(100/500)
        print ("Percentage:",per)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        Area=(height*breadth)/2
        print("Area of Triangle:",Area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth:"))
        perimeter=height1+height2+breadth1
        print("Perimeter of Triangle:",perimeter)
 