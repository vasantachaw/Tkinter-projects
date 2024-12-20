# import qrcode
# str = '''
# artificial intelligence (AI), the ability of a digital computer or computer-controlled robot
# to perform tasks commonly associated with intelligent beings. The term is frequently applied
# to the project of developing systems endowed with the intellectual processes characteristic
# of humans, such as the ability to reason, discover meaning, generalize, or learn from past
# experience. Since the development of the digital computer in the 1940s, it has been demonstrated that
# computers can be programmed to carry out very complex tasks—as, for example, discovering proofs for
#  mathematical theorems or playing chess—with great proficiency. Still, despite continuing advances
#   in computer processing speed and memory capacity, there are as yet no programs that can match human
#    flexibility over wider domains or in tasks requiring much everyday knowledge. On the other hand,
#    some programs have attained the performance levels of human experts and professionals in performing
#     certain specific tasks, so that artificial intelligence in this limited sense is found in applications
#     as diverse as medical diagnosis, computer search engines, and voice or handwriting recognition.

# What is intelligence?
# All but the simplest human behaviour is ascribed to intelligence,
# while even the most complicated insect behaviour is never taken as an indication of intelligence.
#  What is the difference? Consider the behaviour of the digger wasp, Sphex ichneumoneus. When the
#  female wasp returns to her burrow with food, she first deposits it on the threshold, checks for
#  intruders inside her burrow, and only then, if the coast is clear, carries her food inside. The
#   real nature of the wasp’s instinctual behaviour is revealed if the food is moved a few inches
#    away from the entrance to her burrow while she is inside: on emerging, she will repeat the
#    whole procedure as often as the food is displaced. Intelligence—conspicuously absent in the
#    case of Sphex—must include the ability to adapt to new circumstances.

# Psychologists generally do not characterize human intelligence by
# just one trait but by the combination of many diverse abilities. Research in AI
#  has focused chiefly on the following components of intelligence: learning, reasoning, problem
#  solving, perception, and using language.
# '''
# img = qrcode.make(str)
# img.show()

# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some datga')
# qr.make(fit=True)

# img = qr.make_image()


#@ create a barcodes in python
import barcode
barcodes=barcode.get("ean13","151525563635252")
barcodes.save("C:/Users/Death Empire/Desktop/sasd.png")