import json     # to Serialize/Deserialize our syntx.json
#import re       # Regex

# PLEASE READ ALL :

# Bon .. This is just an example to demonstrate how the work is done
# To Go through all the steps Lexer -> Parser -> Evaluator -> Trans to a real PL -> Compile it


# this is the name of the token for variables
# this should be global or a separated json file

Data_Type_Names = {

    # The less the value's chars the more the execution is fast
    "variable_name" : "v",
    "number"        : "n",
    "comment"       : "#"
}

class Lexer(object): # will inherites from Compiler class maybe after ?

    def __init__(self, file , dtypes = "syntx.json"):
        self.tokens = {}
        self.src_file_txt = open(file).readlines()
        self.data_type = json.loads(open(dtypes).read())

        assert self.src_file_txt != None , "[err_code] Invalid Source File .. !"
        assert self.data_type    != None , "[err_code] Invalid Json File .. !"

    
    def start(self , prettyPrint = True):
        '''Start Tokenizing the Source Code of our lang'''
        
        #go through each Line and Enumerate it (to get Line number for stack traceing errors on future)
        for line_number , line_text in enumerate(self.src_file_txt):
            # CHECK IF EMPTY LINE
            if line_text.strip() in ['\n' , '' , ' ', '\t']:
                self.tokens[line_number] = "empty"
            else:
                # tokens[lineNbr] = {'dataType':'value from txt src'}, ...etc
                self.tokens[line_number] = {}

                # 1 - Check if comment .. (starts with #)
                if splitted_text.strip().startswith('#'):
                    self.tokens[line_number][str(line_number)+"_"+str(line_number)] = [Data_Type_Names["comment"] , line_text]
                
                else :
                    #Split the line by spaces (this is a demo so functions and stuff wont work)
                    for dataNumber, splitted_text in enumerate(line_text.split(' ')):
                        # Here we check DtaTypes That wont be in out json file (we can use function of that)
                        
                        # 2 - Check if variable ($VarName like php)
                        if splitted_text.strip().startswith('$'):
                            self.tokens[line_number][str(line_number)+"_"+str(dataNumber)] = [Data_Type_Names["variable_name"] , splitted_text]
                        # 3 - Check if it's a Number
                        elif splitted_text.isnumeric():
                            self.tokens[line_number][str(line_number)+"_"+str(dataNumber)] = [Data_Type_Names["number"] , splitted_text]
                        # 4 - We check Possible cases from our syntx.json
                        else:
                            # looping through the json file keys
                            for __dataType in self.data_type.keys():
                                # Check if basically that text is in one of the datatypes's values we set on json
                                if splitted_text in self.data_type[__dataType]:
                                    self.tokens[line_number][str(line_number)+"_"+str(dataNumber)] = [__dataType , splitted_text]
                                    break
        return self.tokens if not prettyPrint else json.dumps(self.tokens, sort_keys=True, indent=4)