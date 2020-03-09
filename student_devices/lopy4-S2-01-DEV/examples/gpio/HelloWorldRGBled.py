"""
HelloWorldRGBled.py - application to blink the RGB-led of the LoPy4

Application level with 3 styles definied:
- direct execution (Arduino style)
- functional paradigm (Arduino style)
- OOP style (modern programming)

202-03 PP new, added coding styles
firmware v1.20.2.rc6
"""
import blinkingled


def main():
    print("Demo blinking RGB-led...")

    # styles is tuple and specifies the coding style of the application.
    # .. select one of the styles statements
    # styles = (True, False, False)  # Arduino way, direct execution
    # styles = (False, True, False)  # Arduino style, function paradigm
    styles = (False, False, True)  # OOP-style - modern programming

    if styles[0] is True:
        print("\tdirect executed...")
        import blinkingled_direct

    if styles[1] is True:
        from blinkingled import blink
        print("\tfunction blink() executed...")
        blink()

    if styles[2] is True:
        # part 3: OOP - best software engineering
        from blinkingled import RGBLed
        print("\tOOP executed...")
        led = RGBLed()  # create led-object from class RGBLled
        '''
        # call blink, traceback when user interrupts
        led.blink()
        '''
        # try..except for gracefull ending when user interrupts
        try:
            led.blink()
        except KeyboardInterrupt:
            led.off()
            print("\tblinking LED - done!!")
        # '''


if __name__ == '__main__':
    main()
