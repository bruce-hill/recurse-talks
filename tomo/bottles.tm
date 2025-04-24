func sing_bottles(num_bottles:Int)
    for n in num_bottles.to(1)
        if n == 1
            say("One bottle of beer on the wall")
        else
            say("$n bottles of beer on the wall")

    say("No more bottles of beer on the wall!")

func main(n=99)
    sing_bottles(n)
