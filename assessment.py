'''

We want to query an API endpoint to receive data about currently available apartment listings from a rental website. Among the data fields is a column called num_bedrooms, which takes the value of 1 for a "1-bedroom" apartment and 0 for a "studio".

Note: This rental agency only works with studios and 1-bedroom apartments, so there will never be 2+ bedroom listings. Each listing includes information about a "studio" or a "1-bedroom" apartment, so there will never be a listing with both a "studio" and "1-bedroom" offerings in one posting.

The algorithm used occasionally mistags the num_bedrooms value. Specifically, sometimes a "studio" is tagged as having num_bedrooms = 1 or a "1-bedroom" is tagged as num_bedrooms = 0. Further investigation revealed it to be an issue with one of the data fields, description, and the way our algorithm parsed the field to extract a num_bedrooms value.

For example: "description": "Beautiful 1-bedroom apartment with nearby yoga studio." was detected as a yoga studio instead of 1-bedroom and incorrectly had num_bedrooms = 0.

Your task is to write a function that takes in the jsonData and corrects this problem. The GET request retrieves the data as a string which looks like this:

jsonData = [
   {
      "id": "3",
      "agent": "Ton Jett",
      "unit": "#12",
      "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
      "num_bedrooms": 1
   },
   ...
]
While correcting the problem, remember the following edge cases:

If the word "studio" or "1-bedroom" is preceded immediately by any of the words: "yoga", "dance" or "art", don't consider it for num_bedrooms value.
If the description does not contain the word "studio" or "1-bedroom", do not change the value for num_bedrooms.
The rules above should be applied regardless of punctuation or letter casing within the description field.
Your end goal is to return an array of integers representing num_bedrooms for each rental listing, example: [0, 1, 1, 1, 0, 0].

Example

For

jsonData = "[{"id": "1", "agent": "Radulf Katlego", "unit": "#3", "description" : "This luxurious studio apartment is in the heart of downtown.", "num_bedrooms": 1},{"id": "2", "agent": "Kelemen Konrad", "unit": "#36", "description": "We have a 1-bedroom available on the third floor.", "num_bedrooms": 1},{"id": "3", "agent": "Ton Jett", "unit": "#12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num_bedrooms": 1},{"id": "4", "agent": "Fishel Salman", "unit": "#13", "description": "Beautiful studio with a nearby art studio.", "num_bedrooms": 1}]"
the output should be solution(jsonData) = [0, 1, 1, 0].

The above jsonData represents the following JSON:

[
   {
      "id": "1",
      "agent": "Radulf Katlego",
      "unit": "#3",
      "description": "This luxurious studio apartment is in the heart of downtown.",
      "num_bedrooms": 1
   },
   {
      "id": "2",
      "agent": "Kelemen Konrad",
      "unit": "#36",
      "description": "We have a 1-bedroom available on the third floor.",
      "num_bedrooms": 1
   },
   {
      "id": "3",
      "agent": "Ton Jett",
      "unit": "#12",
      "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
      "num_bedrooms": 1
   },
   {
      "id": "4",
      "agent": "Fishel Salman",
      "unit": "#13",
      "description": "Beautiful studio with a nearby art studio.",
      "num_bedrooms": 1
   }
]
Explanation:

In the first listing, description = "This luxurious studio apartment is in the heart of downtown."
"studio" should have num_bedrooms = 0;
In the second listing, description = "We have a 1-bedroom available on the third floor."
"1-bedroom" should have num_bedrooms = 1;
In the third listing, description = "Beautiful 1-bedroom apartment with nearby yoga studio."
"1-bedroom" should have num_bedrooms = 1. Ignore "studio" since it is followed by "yoga".
In the fourth listing, description = "Beautiful studio with a nearby art studio."
"studio" should have num_bedrooms = 0. Ignore the second appearance of "studio" since it is followed by "art".
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string jsonData

String in JSON format. It's guaranteed that each listing contains the fields "id", "agent", "unit", "description" and "num_bedrooms".

Guaranteed constraints:
136 ≤ jsonData.length ≤ 15366.

[output] array.integer

Return an array that contains the correct values for num_bedrooms for all of the listings in jsonData.

Note for Python3 users: if you use a numpy array, casting to a list creates a list of numpy.int64 integers. Your returned array needs to be an array of standard Python int types.

'''

# edge case 1
# If the word "studio" or "1-bedroom" is preceded immediately by any of the words: "yoga", "dance" or "art", don't consider it for num_bedrooms value.

# edge case 2
# If the description does not contain the word "studio" or "1-bedroom", do not change the value for num_bedrooms

# Your end goal is to return an array of integers representing num_bedrooms for each rental listing, example: [0, 1, 1, 1, 0, 0]

def checkDescriptionArt(arr) :
# {
    # print(arr.split())
    desc = arr.split()
    result = False

    if ("yoga" in desc) :
    # {
        result = True
    # }
    
    elif ("dance" in desc) :
    # {
        result = True
    # }
    
    elif ("art" in desc) :
    # {
        result = True
    # }
    
    else :
    # {
        None
    # }

    return result
    
# }

def solution (jsonData) :
# {
    result = [None] * len(jsonData)
    cnt = 0
    
    for i in jsonData :
    # {
        # check if description contains "yoga", "dance" or "art"
        # not checking edge cases that description contains > 1 instance of "studio" or "1-bedroom"
        if (checkDescriptionArt(i["description"])) :
        # {
            None
            # print(i["id"], "hey")
        # }
        
        elif ("studio" in i["description"]) :
        # {
            # print(i["id"], "studio")
            i["num_bedrooms"] = 0
        # }

        elif ("1-bedroom" in i["description"]) :
        # {
            # print(i["id"], "studio")
            i["num_bedrooms"] = 1
        # }

        else :
        # {
            None
        # }

        result[cnt] = i["num_bedrooms"]

        cnt = cnt + 1

    # }

    return result

# }

jsonData = [
            {
                "id": "3",
                "agent": "Ton Jett",
                "unit": "#12",
                "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
                "num_bedrooms": 1
            }
            ]

jsonData = [
            {"id": "1", 
             "agent": "Radulf Katlego", 
             "unit": "#3", 
             "description" : "This luxurious studio apartment is in the heart of downtown.", 
             "num_bedrooms": 1
             },
             {"id": "2",
              "agent": "Kelemen Konrad", 
              "unit": "#36", 
              "description": "We have a 1-bedroom available on the third floor.", 
              "num_bedrooms": 1
              },
              {"id": "3", 
               "agent": "Ton Jett", 
               "unit": "#12", 
               "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", 
               "num_bedrooms": 1
              },
              {"id": "4", 
               "agent": "Fishel Salman", 
               "unit": "#13", 
               "description": "Beautiful studio with a nearby art studio.", 
               "num_bedrooms": 1
              }
              ]

print(solution(jsonData))

'''

********
BONEYARD
********

checkDescription(i["description"])
# ("yoga" in i["description"] or "dance" in i["description"] or "art" in i["description"]) :

    art = ["yoga", "dance", "art"]
        print('!', art in i["description"])
        

# print(jsonData.split())
        # print(i["description"])
        # case1 = "yoga" in i["description"]
        # case2 = "studio" in i["description"]
        # case1 = False
        # case2 = False
        # print(i["id"], case1, case2)
# print(result)
# print(jsonData[1]["description"])

'''