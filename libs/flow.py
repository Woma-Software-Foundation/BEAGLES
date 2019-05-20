#! /usr/bin/env python3

#TODO: Make sure symlinked flow command can find it's resources

import os
import argparse
from darkflow.net.build import TFNet

class Flow(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='[dark]flow translates darknet to tensorflow', add_help=False)
        parser._optionals.title = 'Commands for flow (run command bare to annotate images)'
        main_grp = parser.add_mutually_exclusive_group()
        main_grp.add_argument('--train', default=False, action='store_true',
                            help='train a model on annotated data')
        main_grp.add_argument('--savepb', default=False, action='store_true',
                              help='freeze the model to a .pb')
        main_grp.add_argument('--demo', default='', metavar='', help='demo model on video or webcam')
        main_grp.add_argument('--fbf', default='', metavar='', help='generate frame-by-frame annotation')

        train_grp = parser.add_argument_group('Options for --train')
        train_grp.add_argument('--trainer', default='rmsprop',
                               choices='rmsprop|adadelta|adagrad|adagradDA|momentum|adam|ftrl|sgd', metavar='',
                               help='training algorithm')
        train_grp.add_argument('--momentum', default=0.0, type=float, metavar='',
                            help='applicable for rmsprop and momentum optimizers')
        train_grp.add_argument('--keep', default=20, metavar='N', type=int,
                               help='number of most recent training results to save')
        train_grp.add_argument('--batch', default=16, metavar='N', type=int, help='batch size')
        train_grp.add_argument('--epoch', default=1000, metavar='N', type=int, help='number of epochs')
        train_grp.add_argument('--save', default=32000, metavar='N', type=int,
                               help='save a checkpoint ever N training examples')
        train_grp.add_argument('--lr', default=1e-5, metavar='N', type=float, help='learning rate')
        train_grp.add_argument('--clip', default=False, action='store_true',
                               help='turn on gradient clipping to avoid minima overshoot')

        demo_grp = parser.add_argument_group('Options for flow --demo')
        demo_grp.add_argument('--saveVideo', default='out.avi', metavar='', help='filename of video output')
        demo_grp.add_argument('--queue', default=1, metavar='', help='batch process demo')

        fbf_grp = parser.add_argument_group('Options for --fbf ')
        fbf_grp.add_argument('--lb', '--bbox-size-lower-bound', metavar='[0.01 .. 1.0]', type=float, default=0.0,
                             help='frame-by-frame bounding box perimeter fraction lower bound')

        dirs_grp = parser.add_argument_group('Options that set paths')
        dirs_grp.add_argument('--imgdir', default='../data/sample_img/', metavar='',
                              help='path to testing directory with images')
        dirs_grp.add_argument('--binary', default='../data/bin/', metavar='', help='path to .weights directory')
        dirs_grp.add_argument('--config', default='../data/cfg/', metavar='', help='path to .cfg directory')
        dirs_grp.add_argument('--dataset', default='../data/committedframes', metavar='',
                              help='path to dataset directory')
        dirs_grp.add_argument('--backup', default='../data/ckpt/', metavar='', help='path to checkpoint directory')
        dirs_grp.add_argument('--labels', default='../data/predefined_classes.txt', metavar='',
                              help='path to textfile containing labels')
        dirs_grp.add_argument('--annotation', default='../data/committedframes', metavar='',
                              help='path to the annotation directory')
        dirs_grp.add_argument('--summary', default='../data/summaries/', metavar='',
                              help='path to Tensorboard summaries directory')
        dirs_grp.add_argument('--pbLoad', default='', metavar='*.pb', help='name of protobuf file to load')
        dirs_grp.add_argument('--metaLoad', default='', metavar='',
                            help='path to .meta file generated during --savepb that corresponds to .pb file')
        dirs_grp.add_argument('-l', '--load', default=-1, metavar='', help='filename of weights or checkpoint to load')
        dirs_grp.add_argument('-m', '--model', default='../data/cfg/tiny-yolo-4c.cfg', metavar='',
                              help='filename of model to use')

        opts_grp = parser.add_argument_group('General Options')
        opts_grp.add_argument('--json', default=False, action='store_true',
                              help='output bounding box information in .json')
        opts_grp.add_argument('--gpu', default=0.0, metavar='[0 .. 1.0]', type=float, help='amount of GPU to use')
        opts_grp.add_argument('--gpuName', default='/gpu:0', metavar='/gpu:N', help='GPU device name')
        opts_grp.add_argument('--threshold', default=-0.1, type=float, metavar='[0.01 .. 0.99]',
                            help='threshold of confidence to record an annotation hit')
        opts_grp.add_argument('-v', '--verbalise', default=False, action='store_true',
                              help='show graph structure while building')
        opts_grp.add_argument('-h', '--help', action='help', help='print this message and exit')

        FLAGS = parser.parse_args()

        def _get_dir(dirs):
            for d in dirs:
                this = os.path.abspath(os.path.join(os.path.curdir, d))
                if not os.path.exists(this):
                    os.makedirs(this)

        requiredDirectories = [FLAGS.imgdir, FLAGS.binary, FLAGS.backup, os.path.join(FLAGS.imgdir, 'out')]
        if FLAGS.summary:
            requiredDirectories.append(FLAGS.summary)
        _get_dir(requiredDirectories)
        if FLAGS.gpu > 1.0 or FLAGS.gpu < 0:
            raise ValueError('--gpu should be a number between 0 and 1')
        if FLAGS.threshold < -0.1 or FLAGS.threshold >= 1:
            raise ValueError('--threshold should be a number between 0 and 1 floating point')
        if not FLAGS.save % FLAGS.batch == 0:
            raise ValueError('--save should be a number divisible by the number --batch ')
        try: # TODO: add constraints on FLAGS.gpu range and except: ValueError also add individual error catching for numbers
            FLAGS.save = int(FLAGS.save)
            FLAGS.epoch = int(FLAGS.epoch)
            FLAGS.batch = int(FLAGS.batch)
            FLAGS.threshold = float(FLAGS.threshold)
            FLAGS.gpu = float(FLAGS.gpu)
            FLAGS.lr = float(FLAGS.lr)
        except ValueError:
            print('You should try using numbers instead.')
        try:
            FLAGS.load = int(FLAGS.load)

        except Exception:
            pass  # Non-integer passed as filename using bare except

        tfnet = TFNet(FLAGS)

        if FLAGS.train:
            tfnet.train()
            exit('[INFO] Training finished, exit.')
        elif FLAGS.savepb:
            print('[INFO] Freezing graph of {} at {} to a protobuf file...'.format(FLAGS.model, FLAGS.load))
            tfnet.savepb()
            exit('[INFO] Done')
        elif FLAGS.demo != '':
            tfnet.camera()
        elif FLAGS.fbf != '':
            tfnet.annotate()
        else:
            tfnet.predict()


if __name__ == '__main__':
    Flow()
