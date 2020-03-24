"""
main.py - collection of GPIO examples.
main.py is assembled from various modules.

History
2020-03 PP Smart City semester 2 - template
firmware v1.20.2.rc6 (pybytes)
"""

# execution of the various demos
if __name__ == '__main__':
    print('\nEntering main.py... GPIO demos')

    # activate/deactivate various demo's
    DEMO_BLINKING_RGB = False  # blink RGBLed of the LoPy4
    DEMO_BLINKING_LED = False  # blink external led connected to device
    DEMO_BINAIRE_COUNTER = False  # binaire counter

    #################################
    # execute the GPIO examples
    #################################
    if DEMO_BLINKING_RGB is True:
        from examples.gpio import HelloWorldRGBled
        HelloWorldRGBled.main()

    if DEMO_BLINKING_LED is True:
        print("Blinking externe LED... TODO")
        pass

    if DEMO_BINAIRE_COUNTER is True:
        print("Binaire counter... TODO")

    import gc
    gc.collect()
    print('main(): free memory {} Kb'.format(gc.mem_free() // 1024))
    print('main done')
