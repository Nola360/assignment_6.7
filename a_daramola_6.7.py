#Akinola Daramola Jr
#Programming Exercise 6.7
#Due Date: 07/27/2022



"""
Random Number File Writer
Write a program that writes a series of random numbers to a file.
Each random number should be in the range of 1 through 500.
The application should let the user specify how many random numbers the file will hold.

"""

#Import random library
import random


#Defining mainline() function to run numberGenerator() function
def main():
    #Invoking numberGenerator() function
    numberGenerator()

#Defining numberGenerator() function
def numberGenerator():
        #try block to test for errors
        try:
            #Initializing value of number_count variable
            number_count= 0
            #Specifying amount of numbers file can hold
            specified = int(input("How many numbers will this file contain? "))

            #Iterating through range of numbers specified
            for numbers in range(specified):
                
                #Setting range of random number
                random_number = random.randint(1,501)

                #Number count increments 1 unit for ever random number generated
                number_count += 1

                #Displays number of random numbers generated between 1 - 500
                print(str(f"{number_count}. {random_number}"))

                #Declaring value of file as open("write_file.txt", "a")           
                file = open("write_file.txt", "a")

                #Keeps count of random numbers specified
                number = file.write(str(number_count))

                #Adds dot for number list formatting - example (1. 33) (10. 47) (100. 88)
                dot = file.write(". ")
                
                #Declaring value of each line in file
                numbers = file.write(str(random_number))

                #Adding line break to each iteration of random number generated
                newline = file.write("\n")

                #Closing file
                file.close()

        #Specifying file name and extention type of errors   
        except IOError:
            
            #Display message associated with error type
            print("Error: File does not exist")
            
        #Specifying value entry errors
        except ValueError:
            
            #Display message associated with error type
            print('Error: Invalid entry, please enter a number!')

        #Runs to determine if code was executed
        finally:
            #Display program status message
            print("Program finished executing")

#Invoking main() function to start program    
main()

    
