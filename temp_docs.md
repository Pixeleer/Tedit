# Temp Docs for Creating Levels

## Stringing commands together
To create a level, just attach the commands together with a comma, and save as a *.tlvl* file.

Example: `penc:red,1:25,3:89,loop:loop`

## for

Moves forward the specified amount.

Example: `for:100`

*In this example, the variable after is how many pixels to move.*

## bac

Moves backwards the specified amount.

Example: `bac:50`

*In this example, the variable after is how many pixels to move.*

## r

Turns right the specified amount.

Example: `r:450`

*In this example, the variable after is how many degrees to rotate.*

## l

Turns left the specified amount.

Example: `l:90`

*In this example, the variable after is how many degrees to rotate.*

## loop

Loops back to the beginning infinitely.

Example: `loop:loop`

The second variable can be however you want.

## penc

Changes the pen color to the second variable.

Example: `penc:red`

## cls

Clears the screen.

Example: `cls:cls`

The second variable can be however you want.

## spd

Changes the speed of the pen.

Example: `spd:5`

## w

Waits **in milliseconds**.

Example: `w:1000`

## u

Brings the pen up.

Example: `u:u`

The second variable can be however you want.

## d

Puts the pen back down.

Example: `d:d`

The second variable can be however you want.

## goto

Goes to the position specified.

Example: `goto:400;500`

*In the example, 400 would be the x and 500 would be the y.*

## wrd

Writes text where the cursor is.

Example: `wrd:hello world!`

## c

Sets a checkpoint to go back to later.

Example: `c:c`

The second variable can be however you want.

## gtc
Enables looping and goes back to the last check point placed.


Example: `gtc:gtc`

The second variable can be however you want.

## endl

Disables looping.

Example: `endl:endl`

The second variable can be however you want.