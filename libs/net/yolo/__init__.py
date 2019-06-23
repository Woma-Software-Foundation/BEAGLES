from . import train
from . import predict
from . import data
from . import misc
from ...utils.flags import FlagIO
import numpy as np


""" YOLO framework __init__ equivalent"""

def constructor(self, meta, FLAGS):
	FlagIO.__init__(self, delay=0.5, subprogram=True)
	def _to_color(indx, base):
		""" return (b, r, g) tuple"""
		base2 = base * base
		b = 2 - indx / base2
		r = 2 - (indx % base2) / base
		g = 2 - (indx % base2) % base
		return (b * 127, r * 127, g * 127)
	if 'labels' not in meta:
		misc.labels(meta, FLAGS) #We're not loading from a .pb so we do need to load the labels
	assert len(meta['labels']) == meta['classes'], (
		'labels.txt and {} indicate' + ' '  # TODO: Add error handling for empty classes file
		'inconsistent class numbers'
	).format(meta['model'])

	# assign a color for each label
	colors = list()
	base = int(np.ceil(pow(meta['classes'], 1./3)))
	for x in range(len(meta['labels'])): 
		colors += [_to_color(x, base)]
	meta['colors'] = colors
	self.fetch = list()
	self.meta, self.FLAGS = meta, FLAGS
	self.flags = self.FLAGS

	# over-ride the threshold in meta if FLAGS has it.
	if FLAGS.threshold > 0.0:
		self.meta['thresh'] = FLAGS.threshold