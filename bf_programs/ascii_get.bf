#!../brainfuck.py

The purpose of this program is to print the ascii character
represented by the number provided as standard input


slot 0 will contain the raw input
slot 1 will contain the modified input
slot 2 will contain the decimal place
slot 3 will contain the final number
slot 4 is a temporary info holder used for copying


+   force entry into the loop



[
    ,   store input in slot 0

    [  if the input is not zero
        
        [>+>>>+<<<<-]  move slot 0 into 1 and 4
        >>>>[<<<<+>>>>-] move slot 4 into slot 0
    
        <<<             move to slot 1
        ----- -----
        ----- -----
        ----- -----
        ----- -----
        ----- ---
    

        delete 48 from the storage in slot 1 to convert the ascii
        representation of the integer into its real value


        >[  if slot 2 is not zero then we multiply slot 3 by 10
            
            >[>  set slot 4 = 10 times slot 3
                +++++ +++++
            <-]


            >[<+>-]<   move slot 4 into slot 3

        
            <[-] set slot 2 = 0 to prevent a loop

        ]<



        [>>+<<-]

        add the contents of slot 1 to slot 3
        setting slot 1 = 0 in the process

        >+< set slot 2 = 1

    ]<

]

output the contensts of slot 2
>>>> .
