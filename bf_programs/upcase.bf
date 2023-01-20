#!../brainfuck.py

+   force entry into the loop

[
    ,   store input in slot 0
    [
        [>+>+<<-] move slot 0 to slot 1 and 2
        >>[<<+>>-] move slot 2 to slot 0
        < move to slot 1
        subtract 32
        ----- -----
        ----- -----
        ----- -----
        --
        .[-] print then zero out slot 1
    ]< move back to slot 0
]
