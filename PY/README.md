**THIS IS A PROTOTYPE / DEMO TO SHOW THE BASICS OF HOW WE CAN MAKE OUR PROGRAMMING LANGUAGE**

Making a language is either making a compiler / Transpiler / Interpreter .
So after a meeting we've done we decided to basically make a transpiler instead because :
- Transpiler is faster than a compiler .
- Transpiler is easier than making a compiler:
	- Compiler needss a conversion to machine code.
	- Transpiler does not  since it will Depends on another PL (in this case python) and simply execute the python output.
	
	

**Only Lexer is working now , more to come soon**

> Tokens

	- Tokens are (Key : value ) based , key is either *Line number* or *LineNumber_textData*

			> Example , in our lang we have this block of code with some comments :

			```
				$var = 9 + 9     

				#This is a comment 1
					# this is also a comment 2
												# this is also a comment 3
			```
			> Tokens SHould be :

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


> HOW TO ?

- Install Python 3.x if you have it yet .
- Run main.py  (this will Tokenize the test.lang) and then out put the whole Tokens , which are needed for  next step which is **Parser**

