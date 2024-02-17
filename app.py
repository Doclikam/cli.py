def temp_converter(temp_from, temp_to, temp_value):
    if (temp_from=='FARENHEIGHT' and temp_to=='DEGREE'):
        temp=temp_value- 33.5
        print(f"{temp_value}ferenheight is equal to{temp}in degree celcius!")
    elif (temp_from=='DEGREE' and temp_to=='FARENHEIGHT'):
        temp=temp_value + 33.5
        print(f"{temp_value} in degree celcius is equal to{temp} in farenheight!")

    

temp_from=input("Are you converting from 'farenheight' or 'degrees':").upper()
temp_to=input("Are you converting from 'farenheight' or 'degrees': ").upper()
temp_value=float(input('enter the temperature value: '))

temp_converter(temp_from, temp_to, temp_value)



