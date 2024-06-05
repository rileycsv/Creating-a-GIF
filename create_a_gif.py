import imageio.v3 as iio

filenames = ['duck1.png', 'duck2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('duck.gif', images, duration = 500, loop = 0)