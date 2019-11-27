import numpy as np

#P(A|B) = P(knows the material | answers correctly)
#P(A) = P(knows the material) = 0.6
#P(B) = P(answers correctly)
#P(B|A) = P(answers correctly | knows the material) = 0.85
#P(answers correctly | knows the material) * P(knows the material) OR (+) #P(answers correctly | does not know the material) * P(does not know the material) = 0.59
#P(A|B) = P(B|A) * P(A) / P(B) = 0.86

print(0.85 * 0.6 + 0.2 * 0.4)
print(0.85 * 0.6 / 0.59)