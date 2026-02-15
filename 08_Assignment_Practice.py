if __name__ == '__main__':
    print("Assignment")

    ### Question 1: String Cleaning & Transformation###
    var = "Hi, my name is Rezz!"
    vowels = "aeiou"
    def remove_vowels(text):
        rem = " "
        for ch in text:
            if ch.lower() not in vowels:
                rem = rem + ch
        return rem
    result = remove_vowels(var)
    print(result)

    words = "data engineering rocks"
    def replace_spaces_with_underscores(der):
        return der.replace(" ", "_")

    result = replace_spaces_with_underscores(words)
    print(result)

    course = "data engineering bootcamp"
    def title_case(text1):
        return text1.title()
    output = title_case(course)
    print(output)

    ### Dictionary Aggregation ##
    sales = [
        {"product": "Pen", "amount": 10},
        {"product": "Book", "amount": 20},
        {"product": "Pen", "amount": 15},
        {"product": "Pencil", "amount": 5}
    ]

    def sales_per_record(data):     #defining  function
        totals = {}                                 #creating an empty dictionary in memory
        for record in data:                     #Looping to iterate the record in data
            product = record["product"]     #assigning in loop to, what look inside dictionary and storing it on a variable
            amount = record["amount"]
            if product in totals:                   #now checking if that product is already on totals.
                totals[product] += amount       # if YES, it will add to already listed amount to new amount
            else:
                totals[product] = amount        # if not then it will go to else statement and list product & amount
        return totals                                       #calling the function, means it will stop running when it reached return
    result = sales_per_record(sales)            #storing the function in result and assigning arguments on ()

    for product, total in result.items():           #looping over result to get the output
        print(product + ":", total)                     #using concatenation "+" to join two variables

    ### Q3: Unique Numbers in List ###
    List = [4, 5, 4, 6, 7, 5, 8]

    def unique_numbers(list):       #creating a function which takes the argument as list
        output = []                             #creating a variable to store the output

        for num in list:                        #looping to iterate the list
            if list.count(num) == 1:        # used the count to check how many times the num appeared, if only one time
                output.append(num)          # then storing it to the output variable with append

        return output                                   #returning the output as we only need output

    output = unique_numbers(List)
    print(output)

    ### SQL SECTION ###
    ### Q4.Find the Second - Highest Salary ###
"""    "SELECT DISTINCT salary  AS  Second _Highest_Salary  #selcting distinct salary and using aliasis
"  FROM employees
"    ORDER BY salary DESC    "  # ordering it by salary on descending order
"  LIMIT 1 OFFSET 1 ; "   "                                                          # using offset 1 to skip the first one and using limiting to 1

### Q5. Find Customers with No Orders ###
SELECT c.customer_name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.customers_id IS NULL;
"""
