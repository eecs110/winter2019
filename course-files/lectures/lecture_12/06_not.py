def is_run_slow(button_1_pressed, button_2_pressed):
    return button_1_pressed and not button_2_pressed

def is_fast_run(button_1_pressed, button_2_pressed):
    return button_1_pressed and button_2_pressed


print(is_run_slow(True, True))
print(is_run_slow(True, True))