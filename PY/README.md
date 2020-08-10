**THIS IS A PROTOTYPE / DEMO TO SHOW THE BASICS OF HOW WE CAN MAKE OUR PROGRAMMING LANGUAGE**

Making a language is either making a compiler / Transpiler / Interpreter .
So after a meeting we've done we decided to basically make a transpiler instead because :
- Transpiler is faster than a compiler .
- Transpiler is easier than making a compiler:
	- Compiler needss a conversion to machine code.
	- Transpiler does not  since it will Depends on another PL (in this case python) and simply execute the python output.
	
	

**Only Lexer is working now , more to come soon**

Example , in our lang we have this block of code with some comments :

```
	$var = 9 + 9     

	#This is a comment 1
		# this is also a comment 2
									# this is also a comment 3
```

Tokens SHould be :

```json
{
	"0": {
		"0_0": [
			"v",
			"$var"
		],
		"0_1": [
			"op",
			"="
		],
		"0_2": [
			"n",
			"9"
		],
		"0_3": [
			"op",
			"+"
		],
		"0_4": [
			"n",
			"9"
		]
	},
	"1": "empty",
	"2": [
		"#",
		"#This is a comment 1\n"
	],
	"3": [
		"#",
		"    # this is also a comment 2\n"
	],
	"4": [
		"#",
		"                                # this is also a comment 3"
	]
}

```

> BRIEF EXPLAINATION

- Basically Main keys ("0" , "1" ...etc) represents the lines Numbers .
- "0_0 , 0_1 ...etc" , since we split each line by spaces i kept track of them would be usefull in future .
- And fianlly each sub-dictionary has a list ['data_type' : 'value/text' ] .
	- 'v' simply means Var
	- 'op' means operation symbole
	- 'n' means Number
	- '#' means its an inline comment
	- 'empty' simply means it's an empty line (\n)
- We can know when a line ends simply by checking last item on the line.

> HOW TO ?

- Install Python 3.x if you don't have it yet .
- Run main.py  (this will Tokenize the test.lang into python Tokens ) and then output the whole Tokens , which are needed for  next step which is **Parser**


