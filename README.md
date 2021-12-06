# BEAGLES!

[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://GitHub.com/rjdbcm/BEAGLES/graphs/commit-activity)[![Maintainability](https://api.codeclimate.com/v1/badges/9899a9bd3cdfadaee972/maintainability)](https://codeclimate.com/github/rjdbcm/BEAGLES/maintainability)![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/rjdbcm/BEAGLES)

BEAGLES stands for **BE**havioral **A**nnotation and **G**esture **LE**arning **S**uite, and is intended for behavioral analysis and quantification of video data. The image annotation
GUI was originally forked from [labelImg](https://github.com/tzutalin/labelImg) and the machine learning backend is based on [darkflow](https://github.com/thtrieu/darkflow) but converts darknet configuration files to TensorFlow 2 networks.

|  Branch  |                     Status                     |
|----------|------------------------------------------------|
| master   |[![codecov](https://codecov.io/gh/rjdbcm/BEAGLES/branch/master/graph/badge.svg)](https://codecov.io/gh/rjdbcm/BEAGLES)[![Documentation Status](https://readthedocs.org/projects/beagles/badge/?version=stable)](https://beagles.readthedocs.io/en/stable/?badge=stable)[![Build Status](https://travis-ci.com/rjdbcm/BEAGLES.svg?branch=master)](https://travis-ci.com/rjdbcm/BEAGLES)

## Created Using

[![python](https://img.shields.io/badge/python-3.6%20|%203.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![tensorflow](https://raw.githubusercontent.com/aleen42/badges/master/src/tensorflow.svg?)](https://www.tensorflow.org/)
[![cython](https://img.shields.io/badge/Cython-0.29.6-%23646464)](https://cython.org)
[![numpy](https://img.shields.io/badge/NumPy-1.18-013243)](https://numpy.org/)
[![opencv](https://img.shields.io/badge/OpenCV-4.0-%233a6aeb)](https://opencv.org/)
[![pyqt5](https://img.shields.io/badge/PyQt-5.12-41cd52.svg)](https://pypi.org/project/PyQt5/)

## Features
- Darknet-style configuration files
- Automatic class balance for image classification training
- TensorFlow checkpoint files
- YOLO and VOC annotation formats
- Preconfigured to output training data to TensorBoard
- Fixed or cyclic learning rates 
- Human-in-the-loop prediction and dataset expansion

## Development Goals

- Code coverage of \>60% (*in progress-TF 1.x code caused setbacks*)
- Automatic anchor box generation for YOLO (*in progress*)
- Improve maintainability to A rating (*in progress*)
- [OBS Studio](https://github.com/obsproject/obs-studio) utility for USB camera arrays (*in progress*)
- Statistical report generation using [traces](https://github.com/datascopeanalytics/traces) (*in progress*)
- ~~TensorFlow 2 native code~~ *Done!*

## License

### Free software:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rjdbcm/slgrSuite/blob/master/NOTICE)

### Based in part on original code by: 
- Tzutalin. LabelImg. Git code (2015). https://github.com/tzutalin/labelImg
- Mahmoud Aslan. Cyclic Learning Rate. Git code (2018). https://github.com/mhmoodlan/cyclic-learning-rate

## Created Using:

[![python](https://img.shields.io/badge/python-3.7%20|%203.8-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![tensorflow](https://raw.githubusercontent.com/aleen42/badges/master/src/tensorflow.svg?)](https://www.tensorflow.org/)
[![cython](https://img.shields.io/badge/Cython-0.29.6-%23646464)](https://cython.org)
[![numpy](https://img.shields.io/badge/NumPy-1.18-013243)](https://numpy.org/)
[![opencv](https://img.shields.io/badge/OpenCV-4.0-%233a6aeb)](https://opencv.org/)
[![pyqt5](https://img.shields.io/badge/PyQt-5.12-41cd52.svg)](https://pypi.org/project/PyQt5/)
[![traces](https://img.shields.io/badge/traces-0.5.0-orange.svg)](https://github.com/datascopeanalytics/traces)

## Social

![Twitter Follow](https://img.shields.io/twitter/follow/BEAGLES44967623?label=Follow&style=social)

## Related

- [labelImg](https://github.com/tzutalin/labelImg) the original image annotation software BEAGLES is forked from
- [darkflow](https://github.com/thtrieu/darkflow) the original basis of the machine learning backend
- [cyclic-learning-rate](https://github.com/mhmoodlan/cyclic-learning-rate) the implementation of cyclic learning rates used
- [traces](https://github.com/datascopeanalytics/traces) library for non-transformative unevenly-spaced timeseries analysis
- [OBS Studio](https://github.com/obsproject/obs-studio) video recording software
- [You Only Look Once:Unified, Real-Time Object Detection](https://pjreddie.com/media/files/papers/yolo_1.pdf)
- [YOLO9000: Better, Faster, Stronger](https://pjreddie.com/media/files/papers/YOLO9000.pdf)
- [A Framework for the Analysis of Unevenly Spaced Time Series Data](http://www.eckner.com/papers/unevenly_spaced_time_series_analysis.pdf)
- [Unevenly-spaced data is actually pretty great](https://datascopeanalytics.com/blog/unevenly-spaced-time-series/)
- [Interactive machine learning: experimental evidence for the human in the algorithmic loop](https://link.springer.com/content/pdf/10.1007/s10489-018-1361-5.pdf)
- [Why Momentum Really Works](https://distill.pub/2017/momentum/)

