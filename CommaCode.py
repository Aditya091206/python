print("name:aditya.M,USN:1AY24AI004,sec:'M")
def commacode(items):
    if len(items)==0:
        return''
    elif len(items)==1:
        return items[0]
    else:
        return', '.join(items[:-1])+'and'+ items[-1]
    
my_list=['apples','bananas','tofu','cats']
print(commacode(my_list))