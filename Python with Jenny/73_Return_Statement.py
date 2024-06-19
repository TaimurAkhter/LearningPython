# Date: 5th January 2024 Friday
# Start Time: 08 : 53 PM 
# End Time: 09 : 05 PM 

def add(a, b):
    c = a + b
    return c

result = add(99,152)
print(result)

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # return formatted_f_name, formatted_l_name
    return f"{formatted_f_name} {formatted_l_name}"
    
formatted_name = format_name("TAimUR", "AKHTER")
print(formatted_name)