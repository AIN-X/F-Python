print ()
print('<<<<<<<<<<<<<<<<<<<<<<<<< Python Strings >>>>>>>>>>>>>>>>>>>>>>>>>>')

print(" I am a student ")

print (" I from 'Nachole'")

print("\n"+' Nachole in "Chapainawabgonj"' + "\n")


print('>>>>>>>>>>>>>>>>>>>>>>>>>> Value Assign <<<<<<<<<<<<<<<<<<<<<<<<<')

sf= 'Software'

print ("\n" + sf + "\n")


print('>>>>>>>>>>>>>>>>>>>>>>>>>> Multiline Strings <<<<<<<<<<<<<<<<<<<<<<<<<')

poem =""" In the darkest hour before the dawn,
When all the stars seem to be gone,
A whisper comes, so soft, so bright—
A spark of hope, a gleam of light."""

print("\n"+ poem)

print("\n"+"The poem length is = " + str(len(poem))+"\n")

print('>>>>>>>>>>>>>>>>>>>>>>>>>> Check String <<<<<<<<<<<<<<<<<<<<<<<<<\n')

txt = "This is the simple line taxt"
if "simple" in txt:
    print("This value is here.\n")

print('>>>>>>>>>>>>>>>>>>>>>>>>>> Check if NOT <<<<<<<<<<<<<<<<<<<<<<<<<\n')

txt = "This is the same line taxt"
if "simple" not in txt:
    print("This value is not here.\n")
