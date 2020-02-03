import matplotlib.pyplot as plt
import numpy as np

a=np.array([0.7333323523,0.6234554345322,0.54323252343324,
            0.1413414315465765585,0.43543656543,0.563432525,
            0.545463433,0.832423523423,0.843536363]).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar(shrink=0.9)#高度变成原来的0.9
plt.xticks(())
plt.yticks(())
plt.show()
